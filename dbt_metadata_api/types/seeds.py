from typing import Optional, Union

import strawberry
import strawberry.types
from dbt.contracts.graph.compiled import CompiledSeedNode
from dbt.contracts.graph.parsed import ParsedSeedNode

from dbt_metadata_api.interfaces import NodeInterface, dbtCoreInterface
from dbt_metadata_api.utils import get_manifest

from .common import CatalogColumn
from .utils import get_column_catalogs


@strawberry.type
class SeedNode(NodeInterface, dbtCoreInterface):
    def get_node(
        self, info: strawberry.types.Info
    ) -> Union[ParsedSeedNode, CompiledSeedNode]:
        node = get_manifest(info).nodes[self.unique_id]
        if not isinstance(node, (ParsedSeedNode, CompiledSeedNode)):
            raise ValueError(f"Node with unique_id={self.unique_id} is not a SeedNode")
        return node

    @strawberry.field
    def alias(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).alias

    @strawberry.field
    def children_l1(self, info: strawberry.types.Info) -> Optional[str]:
        return get_manifest(info).child_map[self.unique_id]

    @strawberry.field
    def columns(self, info: strawberry.types.Info) -> Optional[list[CatalogColumn]]:
        return get_column_catalogs(self.get_node(info).columns)

    @strawberry.field
    def compiled_code(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).compiled_code

    @strawberry.field
    def compiled_sql(self, info: strawberry.types.Info) -> Optional[str]:
        if self.get_node(info).language == "sql":
            return self.compiled_code(info)

    @strawberry.field
    def database(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).database

    @strawberry.field
    def raw_code(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).raw_code

    @strawberry.field
    def raw_sql(self, info: strawberry.types.Info) -> Optional[str]:
        if self.get_node(info).language == "sql":
            return self.raw_sql(info)

    @strawberry.field
    def schema(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).schema
