import enum
import inspect
from typing import Any, Optional

import strawberry

from ..models import manifest
from ..scalars import JSONObject

super_rpt = strawberry.experimental.pydantic.fields.replace_pydantic_types


def replace_pydantic_types(type_: Any, is_input: bool) -> Any:
    if inspect.isclass(type_) and issubclass(type_, enum.Enum):
        return strawberry.enum(type_)
    return super_rpt(type_, is_input)


strawberry.experimental.pydantic.fields.replace_pydantic_types = replace_pydantic_types


@strawberry.experimental.pydantic.type(model=manifest.Hook, all_fields=True)
class Hook:
    pass


@strawberry.experimental.pydantic.type(model=manifest.Docs, all_fields=True)
class Docs:
    pass


@strawberry.experimental.pydantic.type(model=manifest.DependsOn, all_fields=True)
class DependsOn:
    pass


@strawberry.experimental.pydantic.type(
    model=manifest.NodeConfig, use_pydantic_alias=False
)
class NodeConfig:
    enabled: strawberry.auto
    alias: strawberry.auto
    schema_: strawberry.auto
    database: strawberry.auto
    tags: Optional[strawberry.scalars.JSON]
    meta: Optional[JSONObject]
    materialized: strawberry.auto
    incremental_strategy: strawberry.auto
    persist_docs: Optional[JSONObject]
    post_hook: Optional[list[Hook]]
    pre_hook: Optional[list[Hook]]
    quoting: Optional[JSONObject]
    column_types: Optional[JSONObject]
    full_refresh: strawberry.auto
    unique_key: Optional[strawberry.scalars.JSON]
    on_schema_change: strawberry.auto
    grants: Optional[JSONObject]
    packages: strawberry.auto
    docs: strawberry.auto


@strawberry.experimental.pydantic.type(
    model=manifest.Quoting,
    all_fields=True,
)
class Quoting:
    pass


@strawberry.experimental.pydantic.type(
    model=manifest.Time,
    all_fields=True,
)
class Time:
    pass


@strawberry.experimental.pydantic.type(model=manifest.ExternalPartition)
class ExternalPartition:
    name: strawberry.auto
    description: strawberry.auto
    data_type: strawberry.auto
    meta: Optional[JSONObject]


@strawberry.experimental.pydantic.type(model=manifest.ExternalTable)
class ExternalTable:
    location: strawberry.auto
    file_format: strawberry.auto
    row_format: strawberry.auto
    tbl_properties: strawberry.auto
    partitions: strawberry.auto


@strawberry.experimental.pydantic.type(
    model=manifest.FreshnessThreshold,
    all_fields=True,
)
class FreshnessThreshold:
    pass


@strawberry.experimental.pydantic.type(model=manifest.FileHash, all_fields=True)
class FileHash:
    pass


@strawberry.experimental.pydantic.type(model=manifest.ColumnInfo, all_fields=True)
class ColumnInfo:
    pass
