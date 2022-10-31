from typing import Optional

from pydantic import BaseModel

from ..interfaces import NodeInterface


def flatten_depends_on(depends_on: BaseModel) -> Optional[list[str]]:
    depends_on = []
    if isinstance(depends_on.macros, str):
        depends_on.append(depends_on.macros)
    else:
        depends_on.extend(depends_on.macros)

    if isinstance(depends_on.nodes, str):
        depends_on.append(depends_on.nodes)
    else:
        depends_on.extend(depends_on.nodes)
        return depends_on


def convert_to_strawberry(
    manifest: BaseModel,
    node: BaseModel,
    expected_resource_type: str = None,
) -> NodeInterface:
    resource_type = node.resource_type.value
    if expected_resource_type is not None:
        resource_type = expected_resource_type

    if resource_type == "model":
        from .models import ModelNode

        cls = ModelNode
    elif resource_type == "exposure":
        from .exposures import ExposureNode

        cls = ExposureNode
    elif resource_type == "macro":
        from .macros import MacroNode

        cls = MacroNode
    elif resource_type == "metric":
        from .metrics import MetricNode

        cls = MetricNode
    elif resource_type == "seed":
        from .seeds import SeedNode

        cls = SeedNode
    elif resource_type == "snapshot":
        from .snapshots import SnapshotNode

        cls = SnapshotNode
    elif resource_type == "test":
        from .tests import TestNode

        cls = TestNode

    return cls(manifest=manifest, unique_id=node.unique_id)
