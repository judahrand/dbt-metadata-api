from typing import Optional

import strawberry
from pydantic import BaseModel

from ..interfaces import NodeInterface, dbtCoreInterface
from ..utils import Manifest
from .utils import flatten_depends_on


@strawberry.type
class MetricFilter:
    field: Optional[str]
    operator: Optional[str]
    value: Optional[str]


@strawberry.type
class MetricNode(NodeInterface, dbtCoreInterface):
    def get_node(self, manifest: Manifest) -> BaseModel:
        return manifest.metrics[self.unique_id]

    @strawberry.field
    def calculation_method(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(
            self.get_node(info.context["manifest"]), "calculation_method", None
        )

    @strawberry.field
    def depends_on(self, info: strawberry.types.Info) -> Optional[list[str]]:
        return flatten_depends_on(self.get_node(info.context["manifest"]).depends_on)

    @strawberry.field
    def dimensions(self, info: strawberry.types.Info) -> Optional[list[str]]:
        return self.get_node(info.context["manifest"]).dimensions

    @strawberry.field
    def expression(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(self.get_node(info.context["manifest"]), "expression", None)

    @strawberry.field
    def filters(self, info: strawberry.types.Info) -> Optional[list[MetricFilter]]:
        return [
            MetricFilter(
                field=filter.field,
                operator=filter.operator,
                value=filter.value,
            )
            for filter in self.get_node(info.context["manifest"]).filters
        ]

    @strawberry.field
    def label(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info.context["manifest"]).label

    @strawberry.field
    def model(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info.context["manifest"]).model

    @strawberry.field
    def sql(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(self.get_node(info.context["manifest"]), "sql", None)

    @strawberry.field
    def time_grains(self, info: strawberry.types.Info) -> Optional[list[str]]:
        return self.get_node(info.context["manifest"]).time_grains

    @strawberry.field
    def timestamp(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info.context["manifest"]).timestamp
