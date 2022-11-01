from typing import TYPE_CHECKING, Annotated, Optional, Union

import strawberry
import strawberry.types
from dbt.contracts.graph.compiled import CompiledSnapshotNode
from dbt.contracts.graph.parsed import ParsedSnapshotNode

from dbt_metadata_api.interfaces import NodeInterface, dbtCoreInterface
from dbt_metadata_api.utils import get_manifest

from .common import CatalogColumn
from .utils import get_column_catalogs, get_parents

if TYPE_CHECKING:
    from .models import ModelNode
    from .sources import SourceNode


@strawberry.type
class SnapshotNode(NodeInterface, dbtCoreInterface):
    def get_node(
        self, info: strawberry.types.Info
    ) -> Union[ParsedSnapshotNode, CompiledSnapshotNode]:
        node = get_manifest(info).nodes[self.unique_id]
        if not isinstance(node, (ParsedSnapshotNode, CompiledSnapshotNode)):
            raise ValueError(f"Node with unique_id={self.unique_id} is not a SeedNode")
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
        return self.get_node(info).compiled_code

    @strawberry.field
    def compiled_sql(self, info: strawberry.types.Info) -> Optional[str]:
        if self.get_node(info).language == "sql":
            return self.compiled_code(info)

    @strawberry.field
    def database(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).database

    @strawberry.field
    def parents_models(
        self, info: strawberry.types.Info
    ) -> Optional[list[Annotated["ModelNode", strawberry.lazy(".models")]]]:
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
