from typing import Optional

import strawberry

from ..interfaces import NodeInterface
from .models import ModelNode


@strawberry.type
class MetricFilter:
    field: Optional[str]
    operator: Optional[str]
    value: Optional[str]


@strawberry.type
class MetricNode(NodeInterface):
    calculation_method: Optional[str]
    depends_on: Optional[list[str]]
    dimensions: Optional[list[str]]
    expression: Optional[str]
    filters: Optional[list[MetricFilter]]
    label: Optional[str]
    model: Optional[ModelNode]
    sql: Optional[str]
    time_grains: Optional[list[str]]
    timestamp: Optional[str]
    type: Optional[str]
