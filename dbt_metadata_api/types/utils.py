from typing import Collection, Dict, List, Optional

from dbt.contracts.graph.manifest import WritableManifest
from dbt.contracts.graph.parsed import ColumnInfo

from dbt_metadata_api.interfaces import NodeInterface
from dbt_metadata_api.types.tests import TestNode

from .common import CatalogColumn


def get_parents(
    unique_id: str,
    manifest: WritableManifest,
    resource_types: Optional[Collection[str]] = None,
) -> List[NodeInterface]:
    possible_parents = {**manifest.nodes, **manifest.sources}
    parents = (
        possible_parents[parent_id] for parent_id in manifest.parent_map[unique_id]
    )
    if resource_types is not None:
        parents = (node for node in parents if node.resource_type in resource_types)

    return [
        convert_to_strawberry(node.unique_id, node.resource_type) for node in parents
    ]


def get_children(
    unique_id: str,
    manifest: WritableManifest,
    resource_types: Optional[Collection[str]] = None,
) -> List[NodeInterface]:
    possible_children = {**manifest.nodes, **manifest.metrics, **manifest.exposures}
    children = (
        possible_children[child_id] for child_id in manifest.parent_map[unique_id]
    )
    if resource_types is not None:
        children = (node for node in children if node.resource_type in resource_types)

    return [
        convert_to_strawberry(node.unique_id, node.resource_type) for node in children
    ]


def get_tests(
    unique_id: str,
    manifest: WritableManifest,
) -> List[TestNode]:
    return [
        convert_to_strawberry(node.unique_id, node.resource_type)
        for node in manifest.nodes.values()
        if node.resource_type == "test" and unique_id in node.depends_on.nodes
    ]


def get_column_catalogs(columns: Dict[str, ColumnInfo]) -> List[CatalogColumn]:
    return [
        CatalogColumn(
            name=col.name,
            index=idx,
            description=col.description,
            meta=col.meta,
            tags=col.tags,
            type=col.data_type,
        )
        for idx, col in enumerate(columns.values())
    ]


def convert_to_strawberry(
    unique_id: str,
    resource_type: str = None,
) -> NodeInterface:
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

    return cls(unique_id=unique_id)
