from typing import TYPE_CHECKING, Annotated, Optional

import strawberry

from ..interfaces import NodeInterface, dbtCoreInterface
from .common import CatalogColumn
from .utils import convert_to_strawberry, flatten_depends_on

if TYPE_CHECKING:
    from .sources import SourceNode
    from .tests import TestNode


@strawberry.type
class ModelNode(NodeInterface, dbtCoreInterface):
    _resource_type: strawberry.Private[str] = "model"

    @strawberry.field
    def alias(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info.context["manifest"]).alias

    @strawberry.field
    def children_l1(self, info: strawberry.types.Info) -> Optional[list[str]]:
        return info.context["manifest"].child_map[self.unique_id]

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
        return getattr(self.get_node(info.context["manifest"]), "compiled_code", None)

    @strawberry.field
    def compiled_sql(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(self.get_node(info.context["manifest"]), "compiled_sql", None)

    @strawberry.field
    def database(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info.context["manifest"]).database

    @strawberry.field
    def depends_on(self, info: strawberry.types.Info) -> Optional[list[str]]:
        if not isinstance(self.get_node(info.context["manifest"]).depends_on, list):
            return flatten_depends_on(
                self.get_node(info.context["manifest"]).depends_on
            )
        return self.get_node(info.context["manifest"]).depends_on

    @strawberry.field
    def materialized_type(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info.context["manifest"]).config.materialized

    @strawberry.field
    def parents_models(
        self, info: strawberry.types.Info
    ) -> Optional[list["ModelNode"]]:
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
        return getattr(self.get_node(info.context["manifest"]), "raw_code", None)

    @strawberry.field
    def raw_sql(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(self.get_node(info.context["manifest"]), "raw_sql", None)

    @strawberry.field
    def schema(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info.context["manifest"]).schema_

    @strawberry.field
    def tests(
        self, info: strawberry.types.Info
    ) -> Optional[list[Annotated["TestNode", strawberry.lazy(".tests")]]]:
        manifest = info.context["manifest"]
        return [
            convert_to_strawberry(unique_id, "test")
            for unique_id, node in manifest.nodes.items()
            if node.resource_type.name == "test"
            and self.unique_id in node.depends_on.nodes
        ]
