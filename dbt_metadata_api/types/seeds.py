from typing import Optional, Union

import strawberry
import strawberry.types
from dbt.contracts.graph.compiled import CompiledSeedNode
from dbt.contracts.graph.parsed import ParsedSeedNode

from ..interfaces import NodeInterface, dbtCoreInterface
from ..utils import get_manifest
from .common import CatalogColumn


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
        manifest = get_manifest(info)
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
            for idx, col in enumerate(self.get_node(info).columns.values())
        ]

    @strawberry.field
    def compiled_code(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(
            self.get_node(info),
            "compiled_code",
            None,
        )

    @strawberry.field
    def compiled_sql(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(
            self.get_node(info),
            "compiled_sql",
            None,
        )

    @strawberry.field
    def database(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).database

    @strawberry.field
    def raw_code(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(
            self.get_node(info),
            "raw_code",
            None,
        )

    @strawberry.field
    def raw_sql(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(
            self.get_node(info),
            "raw_sql",
            None,
        )

    @strawberry.field
    def schema(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).schema_
