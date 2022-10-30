from typing import Optional, Union

import strawberry

from dbt_metadata_api.scalars import Columns, JSONObject

from ..interfaces import NodeInterface
from ..models import manifest


@strawberry.experimental.pydantic.type(model=manifest.TestMetadata)
class TestMetadata:
    name: strawberry.auto
    kwargs: Optional[JSONObject]
    namespace: strawberry.auto


@strawberry.experimental.pydantic.type(model=manifest.TestConfig)
class TestConfig:
    enabled: strawberry.auto
    alias: strawberry.auto
    schema_: strawberry.auto
    database: strawberry.auto
    tags: Optional[strawberry.scalars.JSON]
    meta: Optional[JSONObject]
    materialized: strawberry.auto
    severity: strawberry.auto
    store_failures: strawberry.auto
    where: strawberry.auto
    limit: strawberry.auto
    fail_calc: strawberry.auto
    warn_if: strawberry.auto
    error_if: strawberry.auto


@strawberry.experimental.pydantic.type(model=manifest.ParsedGenericTestNode)
class GenericTestNode(NodeInterface):
    test_metadata: strawberry.auto
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
    name: strawberry.auto
    alias: strawberry.auto
    checksum: strawberry.auto
    config: strawberry.auto
    tags: strawberry.auto
    refs: strawberry.auto
    sources: strawberry.auto
    metrics: strawberry.auto
    depends_on: strawberry.auto
    columns: Optional[Columns]
    meta: Optional[JSONObject]
    docs: strawberry.auto
    patch_path: strawberry.auto
    compiled_path: strawberry.auto
    build_path: strawberry.auto
    deferred: strawberry.auto
    unrendered_config: Optional[JSONObject]
    created_at: strawberry.auto
    config_call_dict: Optional[JSONObject]
    column_name: strawberry.auto
    file_key_name: strawberry.auto


@strawberry.experimental.pydantic.type(model=manifest.ParsedSingularTestNode)
class SingularTestNode(NodeInterface):
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
    name: strawberry.auto
    alias: strawberry.auto
    checksum: strawberry.auto
    config: strawberry.auto
    tags: strawberry.auto
    refs: strawberry.auto
    sources: strawberry.auto
    metrics: strawberry.auto
    depends_on: strawberry.auto
    columns: Optional[Columns]
    meta: Optional[JSONObject]
    docs: strawberry.auto
    patch_path: strawberry.auto
    compiled_path: strawberry.auto
    build_path: strawberry.auto
    deferred: strawberry.auto
    unrendered_config: Optional[JSONObject]
    created_at: strawberry.auto
    config_call_dict: Optional[JSONObject]


TestNode = Union[GenericTestNode, SingularTestNode]
