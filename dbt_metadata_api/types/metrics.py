from typing import Optional

import strawberry
import strawberry.types
from dbt.contracts.graph.parsed import ParsedMetric

from ..interfaces import NodeInterface, dbtCoreInterface
from ..utils import get_manifest


@strawberry.type
class MetricFilter:
    field: Optional[str]
    operator: Optional[str]
    value: Optional[str]


@strawberry.type
class MetricNode(NodeInterface, dbtCoreInterface):
    def get_node(self, info: strawberry.types.Info) -> ParsedMetric:
        return get_manifest(info).metrics[self.unique_id]

    @strawberry.field
    def calculation_method(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(self.get_node(info), "calculation_method", None)

    @strawberry.field
    def depends_on(self, info: strawberry.types.Info) -> Optional[list[str]]:
        return self.get_node(info).depends_on_nodes

    @strawberry.field
    def dimensions(self, info: strawberry.types.Info) -> Optional[list[str]]:
        return self.get_node(info).dimensions

    @strawberry.field
    def expression(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(self.get_node(info), "expression", None)

    @strawberry.field
    def filters(self, info: strawberry.types.Info) -> Optional[list[MetricFilter]]:
        return [
            MetricFilter(
                field=filter.field,
                operator=filter.operator,
                value=filter.value,
            )
            for filter in self.get_node(info).filters
        ]

    @strawberry.field
    def label(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).label

    @strawberry.field
    def model(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).model

    @strawberry.field
    def sql(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(self.get_node(info), "sql", None)

    @strawberry.field
    def time_grains(self, info: strawberry.types.Info) -> Optional[list[str]]:
        return self.get_node(info).time_grains

    @strawberry.field
    def timestamp(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).timestamp
