from typing import Optional
from pydantic import BaseModel

import strawberry

from ..enums import TimePeriod
from ..interfaces import NodeInterface, dbtCoreInterface
from .common import CatalogColumn, Criteria, CriteriaInfo
from ..utils import Manifest


@strawberry.type
class SourceNode(NodeInterface, dbtCoreInterface):
    _resource_type: strawberry.Private[str] = "source"

    def get_node(self, manifest: Manifest) -> BaseModel:
        return manifest.sources[self.unique_id]

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
    def criteria(self, info: strawberry.types.Info) -> Optional[Criteria]:
        node = self.get_node(info.context["manifest"])
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
        return self.get_node(info.context["manifest"]).database

    @strawberry.field
    def identifier(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info.context["manifest"]).identifier

    @strawberry.field
    def loader(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info.context["manifest"]).loader

    @strawberry.field
    def schema(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info.context["manifest"]).schema_

    @strawberry.field
    def source_description(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info.context["manifest"]).source_description

    @strawberry.field
    def source_name(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info.context["manifest"]).source_name
