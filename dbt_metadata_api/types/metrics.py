from typing import Optional

import strawberry
from pydantic import BaseModel

from ..interfaces import NodeInterface
from .utils import flatten_depends_on


@strawberry.type
class MetricFilter:
    field: Optional[str]
    operator: Optional[str]
    value: Optional[str]


@strawberry.type
class MetricNode(NodeInterface):

    @property
    def node(self) -> BaseModel:
        return self.manifest.metrics[self.unique_id]

    @strawberry.field
    def calculation_method(self) -> Optional[str]:
        return self.node.calculation_method

    @strawberry.field
    def depends_on(self) -> Optional[list[str]]:
        return flatten_depends_on(self.node.depends_on)

    @strawberry.field
    def dimensions(self) -> Optional[list[str]]:
        return self.node.dimensions

    @strawberry.field
    def expression(self) -> Optional[str]:
        return self.node.expression

    @strawberry.field
    def filters(self) -> Optional[list[MetricFilter]]:
        return [
            MetricFilter(
                field=filter.field,
                operator=filter.operator,
                value=filter.value,
            )
            for filter in self.node.filters
        ]

    @strawberry.field
    def label(self) -> Optional[str]:
        return self.node.label

    @strawberry.field
    def model(self) -> Optional[str]:
        return self.node.model

    @strawberry.field
    def sql(self) -> Optional[str]:
        return getattr(
            self.node,
            "sql",
            self.node.expression,
        )

    @strawberry.field
    def time_grains(self) -> Optional[list[str]]:
        return self.node.time_grains

    @strawberry.field
    def timestamp(self) -> Optional[str]:
        return self.node.timestamp
