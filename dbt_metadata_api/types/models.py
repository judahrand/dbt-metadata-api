from typing import TYPE_CHECKING, Annotated, Optional

import strawberry

from ..interfaces import NodeInterface
from .common import CatalogColumn
from .utils import convert_to_strawberry, flatten_depends_on

if TYPE_CHECKING:
    from .sources import SourceNode
    from .tests import TestNode


@strawberry.type
class ModelNode(NodeInterface):
    def __post_init__(self) -> None:
        if self.node.resource_type.value != "model":
            raise TypeError("That unique_id is not a model.")

    @strawberry.field
    def alias(self) -> Optional[str]:
        return self.node.alias

    @strawberry.field
    def children_l1(self) -> Optional[list[str]]:
        return self.manifest.child_map[self.unique_id]

    @strawberry.field
    def columns(self) -> Optional[list[CatalogColumn]]:
        return [
            CatalogColumn(
                name=col.name,
                index=idx,
                description=col.description,
                meta=col.meta,
                tags=col.tags,
                type=col.data_type,
            )
            for idx, col in enumerate(self.node.columns.values())
        ]

    @strawberry.field
    def compiled_code(self) -> Optional[str]:
        return self.node.compiled_code

    @strawberry.field
    def compiled_sql(self) -> Optional[str]:
        if getattr(self.node, "language", "sql") == "sql":
            return self.compiled_code()
        return None

    @strawberry.field
    def database(self) -> Optional[str]:
        return self.node.database

    @strawberry.field
    def depends_on(self) -> Optional[list[str]]:
        return flatten_depends_on(self.node.depends_on)

    @strawberry.field
    def materialized_type(self) -> Optional[str]:
        return self.node.config.materialized

    @strawberry.field
    def parents_models(self) -> Optional[list["ModelNode"]]:
        parents = self.manifest.parent_map[self.unique_id]
        return [
            convert_to_strawberry(self.manifest, unique_id)
            for unique_id in parents
            if self.manifest.nodes[unique_id].resource_type.value == "model"
        ]

    @strawberry.field
    def parents_sources(
        self,
    ) -> Optional[list[Annotated["SourceNode", strawberry.lazy(".sources")]]]:
        parents = self.manifest.parent_map[self.unique_id]
        return [
            convert_to_strawberry(self.manifest, unique_id)
            for unique_id in parents
            if self.manifest.nodes[unique_id].resource_type.value == "source"
        ]

    @strawberry.field
    def raw_code(self) -> Optional[str]:
        return self.node.raw_code

    @strawberry.field
    def raw_sql(self) -> Optional[str]:
        if getattr(self.node, "language", "sql") == "sql":
            return self.raw_code()
        return None

    @strawberry.field
    def schema(self) -> Optional[str]:
        return self.node.schema_

    @strawberry.field
    def tests(self) -> Optional[list[Annotated["TestNode", strawberry.lazy(".tests")]]]:
        return [
            convert_to_strawberry(self.manifest, node.unique_id)
            for node in self.manifest.nodes.values()
            if node.resource_type.value == "test"
            and self.unique_id in node.depends_on.nodes
        ]
