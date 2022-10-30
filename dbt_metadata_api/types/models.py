from typing import Optional

import strawberry

from ..interfaces import NodeInterface
from ..models import manifest
from ..scalars import Columns, JSONObject


@strawberry.experimental.pydantic.type(model=manifest.ParsedModelNode)
class ModelNode(NodeInterface):
    database: strawberry.auto
    schema_: strawberry.auto
    fqn: strawberry.auto
    unique_id: strawberry.auto
    raw_code: strawberry.auto
    language: strawberry.auto
    package_name: strawberry.auto
    root_path: strawberry.auto
    path: strawberry.auto
    original_file_path: strawberry.auto
    alias: strawberry.auto
    checksum: strawberry.auto
    config: strawberry.auto
    refs: strawberry.auto
    sources: strawberry.auto
    metrics: strawberry.auto
    depends_on: strawberry.auto
    columns: Optional[Columns]
    docs: strawberry.auto
    patch_path: strawberry.auto
    compiled_path: strawberry.auto
    build_path: strawberry.auto
    deferred: strawberry.auto
    unrendered_config: Optional[JSONObject]
    created_at: strawberry.auto
    config_call_dict: Optional[JSONObject]
