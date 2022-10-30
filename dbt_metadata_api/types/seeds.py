from typing import Optional

import strawberry

from ..interfaces import NodeInterface
from ..models import manifest
from ..scalars import Columns, JSONObject


@strawberry.experimental.pydantic.type(
    model=manifest.SeedConfig, use_pydantic_alias=False
)
class SeedConfig:
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
    full_refresh: Optional[bool] = None
    unique_key: Optional[strawberry.scalars.JSON]
    on_schema_change: Optional[str]
    grants: Optional[JSONObject]
    packages: strawberry.auto
    docs: strawberry.auto
    quote_columns: strawberry.auto


@strawberry.experimental.pydantic.type(model=manifest.ParsedSeedNode)
class SeedNode(NodeInterface):
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
    refs: Optional[strawberry.scalars.JSON]
    sources: Optional[strawberry.scalars.JSON]
    metrics: Optional[strawberry.scalars.JSON]
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
