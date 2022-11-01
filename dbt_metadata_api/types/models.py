from typing import TYPE_CHECKING, Annotated, Optional, Union

import strawberry
import strawberry.types
from dbt.contracts.graph.compiled import CompiledModelNode
from dbt.contracts.graph.parsed import ParsedModelNode

from dbt_metadata_api.interfaces import NodeInterface, dbtCoreInterface
from dbt_metadata_api.utils import get_manifest

from .common import CatalogColumn
from .utils import get_column_catalogs, get_parents, get_tests

if TYPE_CHECKING:
    from .sources import SourceNode
    from .tests import TestNode


@strawberry.type
class ModelNode(NodeInterface, dbtCoreInterface):
    def get_node(
        self, info: strawberry.types.Info
    ) -> Union[ParsedModelNode, CompiledModelNode]:
        node = get_manifest(info).nodes[self.unique_id]
        if not isinstance(node, (ParsedModelNode, CompiledModelNode)):
            raise ValueError(f"Node with unique_id={self.unique_id} is not a ModelNode")
        return node

    @strawberry.field
    def alias(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).alias

    @strawberry.field
    def children_l1(self, info: strawberry.types.Info) -> Optional[list[str]]:
        return get_manifest(info).child_map[self.unique_id]

    @strawberry.field
    def columns(self, info: strawberry.types.Info) -> Optional[list[CatalogColumn]]:
        return get_column_catalogs(self.get_node(info).columns)

    @strawberry.field
    def compiled_code(self, info: strawberry.types.Info) -> Optional[str]:
        node = self.get_node(info)
        if isinstance(node, CompiledModelNode):
            return self.get_node(info).compiled_code

    @strawberry.field
    def compiled_sql(self, info: strawberry.types.Info) -> Optional[str]:
        if self.get_node(info).language == "sql":
            return self.compiled_code(info)

    @strawberry.field
    def database(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).database

    @strawberry.field
    def depends_on(self, info: strawberry.types.Info) -> Optional[list[str]]:
        self.get_node(info).depends_on_nodes

    @strawberry.field
    def materialized_type(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).config.materialized

    @strawberry.field
    def parents_models(
        self, info: strawberry.types.Info
    ) -> Optional[list["ModelNode"]]:
        return get_parents(
            self.unique_id, get_manifest(info), resource_types=("model",)
        )

    @strawberry.field
    def parents_sources(
        self,
        info: strawberry.types.Info,
    ) -> Optional[list[Annotated["SourceNode", strawberry.lazy(".sources")]]]:
        return get_parents(
            self.unique_id, get_manifest(info), resource_types=("source",)
        )

    @strawberry.field
    def raw_code(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).raw_code

    @strawberry.field
    def raw_sql(self, info: strawberry.types.Info) -> Optional[str]:
        if self.get_node(info).language == "sql":
            return self.raw_code(info)

    @strawberry.field
    def schema(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).schema

    @strawberry.field
    def tests(
        self, info: strawberry.types.Info
    ) -> Optional[list[Annotated["TestNode", strawberry.lazy(".tests")]]]:
        return get_tests(self.unique_id, get_manifest(info))
