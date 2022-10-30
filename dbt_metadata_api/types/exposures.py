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


@strawberry.experimental.pydantic.type(model=manifest.ExposureOwner, all_fields=True)
class ExposureOwner:
    pass


@strawberry.experimental.pydantic.type(model=manifest.ExposureConfig, all_fields=True)
class ExposureConfig:
    pass


@strawberry.experimental.pydantic.type(model=manifest.ParsedExposure)
class ExposureNode(NodeInterface):
    fqn: strawberry.auto
    package_name: strawberry.auto
    root_path: strawberry.auto
    path: strawberry.auto
    original_file_path: strawberry.auto
    name: strawberry.auto
    type: strawberry.auto
    owner: strawberry.auto
    resource_type: strawberry.auto
    description: strawberry.auto
    label: strawberry.auto
    maturity: strawberry.auto
    meta: Optional[JSONObject]
    tags: strawberry.auto
    config: strawberry.auto
    unrendered_config: Optional[JSONObject]
    url: strawberry.auto
    depends_on: strawberry.auto
    refs: strawberry.auto
    sources: strawberry.auto
    created_at: strawberry.auto
