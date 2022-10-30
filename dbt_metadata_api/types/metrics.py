import enum
import inspect
from typing import Any, Optional

import strawberry

from ..interfaces import NodeInterface
from ..models import manifest
from ..scalars import JSONObject
from . import common

super_rpt = strawberry.experimental.pydantic.fields.replace_pydantic_types


def replace_pydantic_types(type_: Any, is_input: bool) -> Any:
    if inspect.isclass(type_) and issubclass(type_, enum.Enum):
        return strawberry.enum(type_)
    return super_rpt(type_, is_input)


strawberry.experimental.pydantic.fields.replace_pydantic_types = replace_pydantic_types


@strawberry.experimental.pydantic.type(model=manifest.MetricFilter, all_fields=True)
class MetricFilter:
    pass


@strawberry.experimental.pydantic.type(model=manifest.MetricTime, all_fields=True)
class MetricTime:
    pass


@strawberry.experimental.pydantic.type(model=manifest.MetricConfig, all_fields=True)
class MetricConfig:
    pass


@strawberry.experimental.pydantic.type(model=manifest.ParsedMetric)
class MetricNode(NodeInterface):
    fqn: strawberry.auto
    unique_id: str = strawberry.auto
    package_name: strawberry.auto
    root_path: strawberry.auto
    path: strawberry.auto
    original_file_path: strawberry.auto
    label: strawberry.auto
    calculation_method: strawberry.auto
    expression: strawberry.auto
    timestamp: strawberry.auto
    filters: strawberry.auto
    time_grains: strawberry.auto
    dimensions: strawberry.auto
    window: strawberry.auto
    model: strawberry.auto
    model_unique_id: strawberry.auto
    config: strawberry.auto
    unrendered_config: Optional[JSONObject]
    sources: strawberry.auto
    depends_on: strawberry.auto
    refs: strawberry.auto
    metrics: strawberry.auto
    created_at: strawberry.auto
