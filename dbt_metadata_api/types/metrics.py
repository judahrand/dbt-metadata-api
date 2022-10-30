from typing import Optional
from pydantic import BaseModel

import strawberry

from ..interfaces import NodeInterface


@strawberry.type
class MetricFilter:
    field: Optional[str]
    operator: Optional[str]
    value: Optional[str]


@strawberry.type
class MetricNode(NodeInterface):

    def __post_init__(self) -> None:
        if self.node.resource_type.value != "metric":
            raise TypeError("That unique_id is not a metric.")

    @property
    def node(self) -> BaseModel:
        return self.manifest.metrics[self.unique_id]

    @strawberry.field
    def calculation_method(self) -> Optional[str]:
        return self.node.calculation_method

    @strawberry.field
    def depends_on(self) -> Optional[list[str]]:
        depends_on = []
        if isinstance(self.node.depends_on.macros, str):
            depends_on.append(self.node.depends_on.macros)
        else:
            depends_on.extend(self.node.depends_on.macros)

        if isinstance(self.node.depends_on.nodes, str):
            depends_on.append(self.node.depends_on.nodes)
        else:
            depends_on.extend(self.node.depends_on.nodes)
        return depends_on

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
            for filter in
            self.node.filters
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
