from typing import Optional

import strawberry
from dbt.contracts.graph.manifest import WritableManifest
from pydantic import BaseModel

from ..enums import TimePeriod
from ..interfaces import NodeInterface, dbtCoreInterface
from ..utils import get_manifest
from .common import CatalogColumn, Criteria, CriteriaInfo


@strawberry.type
class SourceNode(NodeInterface, dbtCoreInterface):
    _resource_type: strawberry.Private[str] = "source"

    def get_node(self, manifest: WritableManifest) -> BaseModel:
        return manifest.sources[self.unique_id]

    @strawberry.field
    def children_l1(self, info: strawberry.types.Info) -> Optional[list[str]]:
        manifest = get_manifest(info.context)
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
                self.get_node(get_manifest(info.context)).columns.values()
            )
        ]

    @strawberry.field
    def criteria(self, info: strawberry.types.Info) -> Optional[Criteria]:
        node = self.get_node(get_manifest(info.context))
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
        return self.get_node(get_manifest(info.context)).database

    @strawberry.field
    def identifier(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).identifier

    @strawberry.field
    def loader(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).loader

    @strawberry.field
    def schema(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).schema_

    @strawberry.field
    def source_description(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).source_description

    @strawberry.field
    def source_name(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).source_name
