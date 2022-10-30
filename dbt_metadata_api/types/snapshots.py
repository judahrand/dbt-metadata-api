from typing import Optional

import strawberry

from ..interfaces import NodeInterface
from ..models import manifest
from ..scalars import Columns, JSONObject


@strawberry.experimental.pydantic.type(
    model=manifest.SnapshotConfig, use_pydantic_alias=False
)
class SnapshotConfig:
    enabled: strawberry.auto
    alias: strawberry.auto
    schema_: strawberry.auto
    database: strawberry.auto
    tags: Optional[strawberry.scalars.JSON]
    meta: Optional[JSONObject]
    materialized: strawberry.auto
    incremental_strategy: strawberry.auto
    persist_docs: Optional[JSONObject]
    post_hook: strawberry.auto
    pre_hook: strawberry.auto
    quoting: Optional[JSONObject]
    column_types: Optional[JSONObject]
    full_refresh: strawberry.auto
    unique_key: strawberry.auto
    on_schema_change: strawberry.auto
    grants: Optional[JSONObject]
    packages: strawberry.auto
    docs: strawberry.auto
    strategy: strawberry.auto
    target_schema: strawberry.auto
    target_database: strawberry.auto
    updated_at: strawberry.auto
    check_cols: Optional[strawberry.scalars.JSON]


@strawberry.experimental.pydantic.type(model=manifest.ParsedSnapshotNode)
class SnapshotNode(NodeInterface):
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
    description: strawberry.auto
    columns: Optional[Columns]
    docs: strawberry.auto
    patch_path: strawberry.auto
    compiled_path: strawberry.auto
    build_path: strawberry.auto
    deferred: strawberry.auto
    unrendered_config: Optional[JSONObject]
    created_at: strawberry.auto
    config_call_dict: Optional[JSONObject]
