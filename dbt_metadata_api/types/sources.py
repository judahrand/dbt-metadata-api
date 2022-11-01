from typing import Optional

import strawberry
import strawberry.types
from dbt.contracts.graph.parsed import ParsedSourceDefinition

from dbt_metadata_api.interfaces import NodeInterface, dbtCoreInterface
from dbt_metadata_api.utils import get_manifest

from ..enums import TimePeriod
from .common import CatalogColumn, Criteria, CriteriaInfo


@strawberry.type
class SourceNode(NodeInterface, dbtCoreInterface):
    def get_node(self, info: strawberry.types.Info) -> ParsedSourceDefinition:
        return get_manifest(info).sources[self.unique_id]

    @strawberry.field
    def children_l1(self, info: strawberry.types.Info) -> Optional[list[str]]:
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
    def criteria(self, info: strawberry.types.Info) -> Optional[Criteria]:
        node = self.get_node(info)
        return Criteria(
            error_after=CriteriaInfo(
                count=node.freshness.error_after.count,
                period=TimePeriod(node.freshness.error_after.period),
            ),
            warn_after=CriteriaInfo(
                count=node.freshness.warn_after.count,
                period=TimePeriod(node.freshness.warn_after.count),
            ),
        )

    @strawberry.field
    def database(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).database

    @strawberry.field
    def identifier(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).identifier

    @strawberry.field
    def loader(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).loader

    @strawberry.field
    def schema(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).schema

    @strawberry.field
    def source_description(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).source_description

    @strawberry.field
    def source_name(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).source_name
