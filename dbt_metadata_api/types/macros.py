import enum
import inspect
from typing import Any

import strawberry

from ..interfaces import NodeInterface
from ..models import manifest

super_rpt = strawberry.experimental.pydantic.fields.replace_pydantic_types


def replace_pydantic_types(type_: Any, is_input: bool) -> Any:
    if inspect.isclass(type_) and issubclass(type_, enum.Enum):
        return strawberry.enum(type_)
    return super_rpt(type_, is_input)


strawberry.experimental.pydantic.fields.replace_pydantic_types = replace_pydantic_types


@strawberry.experimental.pydantic.type(model=manifest.MacroArgument, all_fields=True)
class MacroArgument:
    pass


@strawberry.experimental.pydantic.type(model=manifest.MacroDependsOn, all_fields=True)
class MacroDependsOn:
    pass


@strawberry.experimental.pydantic.type(model=manifest.ParsedMacro)
class MacroNode(NodeInterface):
    unique_id: strawberry.auto
    package_name: strawberry.auto
    root_path: strawberry.auto
    path: strawberry.auto
    original_file_path: strawberry.auto
    name: strawberry.auto
    macro_sql: strawberry.auto
    resource_type: strawberry.auto
    depends_on: strawberry.auto
    description: strawberry.auto
    docs: strawberry.auto
    patch_path: strawberry.auto
    arguments: strawberry.auto
    created_at: strawberry.auto
    supported_languages: strawberry.auto
