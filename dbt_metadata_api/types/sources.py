import enum
import inspect
from typing import Any, Optional

import strawberry

from ..interfaces import NodeInterface
from ..models import manifest
from ..scalars import Columns, JSONObject

super_rpt = strawberry.experimental.pydantic.fields.replace_pydantic_types


def replace_pydantic_types(type_: Any, is_input: bool) -> Any:
    if inspect.isclass(type_) and issubclass(type_, enum.Enum):
        return strawberry.enum(type_)
    return super_rpt(type_, is_input)


strawberry.experimental.pydantic.fields.replace_pydantic_types = replace_pydantic_types


@strawberry.experimental.pydantic.type(
    model=manifest.SourceConfig,
    all_fields=True,
)
class SourceConfig:
    pass


@strawberry.experimental.pydantic.type(model=manifest.ParsedSourceDefinition)
class SourceNode(NodeInterface):
    fqn: strawberry.auto
    database: strawberry.auto
    schema_: strawberry.auto
    unique_id: strawberry.auto
    package_name: strawberry.auto
    root_path: strawberry.auto
    path: strawberry.auto
    original_file_path: strawberry.auto
    name: strawberry.auto
    source_name: strawberry.auto
    source_description: strawberry.auto
    loader: strawberry.auto
    identifier: strawberry.auto
    quoting: strawberry.auto
    loaded_at_field: strawberry.auto
    freshness: strawberry.auto
    external: strawberry.auto
    description: strawberry.auto
    columns: Optional[Columns]
    source_meta: Optional[JSONObject]
    config: strawberry.auto
    patch_path: strawberry.auto
    unrendered_config: Optional[JSONObject]
    relation_name: strawberry.auto
    created_at: strawberry.auto
