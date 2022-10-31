from typing import TYPE_CHECKING, Annotated, Optional

import strawberry

from ..interfaces import NodeInterface, dbtCoreInterface
from .common import CatalogColumn
from .utils import convert_to_strawberry

if TYPE_CHECKING:
    from .models import ModelNode
    from .sources import SourceNode


@strawberry.type
class SnapshotNode(NodeInterface, dbtCoreInterface):
    _resource_type: strawberry.Private[str] = "snapshot"

    @strawberry.field
    def alias(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info.context["manifest"]).alias

    @strawberry.field
    def children_l1(self, info: strawberry.types.Info) -> Optional[list[str]]:
        manifest = info.context["manifest"]
        return manifest.child_map[self.unique_id]

    @strawberry.field
    def columns(self, info: strawberry.types.Info) -> Optional[list[CatalogColumn]]:
        return [
            CatalogColumn(
                name=col.name,
                index=idx,
                description=col.description,
                meta=col.meta,
                tags=col.tags,
                type=col.data_type,
            )
            for idx, col in enumerate(
                self.get_node(info.context["manifest"]).columns.values()
            )
        ]

    @strawberry.field
    def compiled_code(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(
            self.get_node(info.context["manifest"]),
            "compiled_code",
            None,
        )

    @strawberry.field
    def compiled_sql(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(
            self.get_node(info.context["manifest"]),
            "compiled_sql",
            None,
        )

    @strawberry.field
    def database(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info.context["manifest"]).database

    @strawberry.field
    def parents_models(
        self, info: strawberry.types.Info
    ) -> Optional[list[Annotated["ModelNode", strawberry.lazy(".models")]]]:
        manifest = info.context["manifest"]
        parents = manifest.parent_map[self.unique_id]
        return [
            convert_to_strawberry(unique_id, "model")
            for unique_id in parents
            if manifest.nodes[unique_id].resource_type.name == "model"
        ]

    @strawberry.field
    def parents_sources(
        self,
        info: strawberry.types.Info,
    ) -> Optional[list[Annotated["SourceNode", strawberry.lazy(".sources")]]]:
        manifest = info.context["manifest"]
        parents = manifest.parent_map[self.unique_id]
        return [
            convert_to_strawberry(unique_id, "source")
            for unique_id in parents
            if manifest.nodes[unique_id].resource_type.name == "source"
        ]

    @strawberry.field
    def raw_code(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(
            self.get_node(info.context["manifest"]),
            "raw_code",
            None,
        )

    @strawberry.field
    def raw_sql(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(
            self.get_node(info.context["manifest"]),
            "raw_sql",
            None,
        )

    @strawberry.field
    def schema(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info.context["manifest"]).schema_
