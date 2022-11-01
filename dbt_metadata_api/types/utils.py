from ..interfaces import NodeInterface


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
