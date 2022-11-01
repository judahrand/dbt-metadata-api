from typing import Optional

import strawberry
from dbt.contracts.graph.manifest import WritableManifest
from pydantic import BaseModel

from ..interfaces import NodeInterface, dbtCoreInterface
from ..utils import get_manifest
from .utils import flatten_depends_on


@strawberry.type
class MetricFilter:
    field: Optional[str]
    operator: Optional[str]
    value: Optional[str]


@strawberry.type
class MetricNode(NodeInterface, dbtCoreInterface):
    _resource_type: strawberry.Private[str] = "metric"

    def get_node(self, manifest: WritableManifest) -> BaseModel:
        return manifest.metrics[self.unique_id]

    @strawberry.field
    def calculation_method(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(
            self.get_node(get_manifest(info.context)), "calculation_method", None
        )

    @strawberry.field
    def depends_on(self, info: strawberry.types.Info) -> Optional[list[str]]:
        return flatten_depends_on(self.get_node(get_manifest(info.context)).depends_on)

    @strawberry.field
    def dimensions(self, info: strawberry.types.Info) -> Optional[list[str]]:
        return self.get_node(get_manifest(info.context)).dimensions

    @strawberry.field
    def expression(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(self.get_node(get_manifest(info.context)), "expression", None)

    @strawberry.field
    def filters(self, info: strawberry.types.Info) -> Optional[list[MetricFilter]]:
        return [
            MetricFilter(
                field=filter.field,
                operator=filter.operator,
                value=filter.value,
            )
            for filter in self.get_node(get_manifest(info.context)).filters
        ]

    @strawberry.field
    def label(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).label

    @strawberry.field
    def model(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).model

    @strawberry.field
    def sql(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(self.get_node(get_manifest(info.context)), "sql", None)

    @strawberry.field
    def time_grains(self, info: strawberry.types.Info) -> Optional[list[str]]:
        return self.get_node(get_manifest(info.context)).time_grains

    @strawberry.field
    def timestamp(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).timestamp
