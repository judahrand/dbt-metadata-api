from __future__ import annotations

from typing import List, Optional

import strawberry

from .enums import ResourceType
from .models import manifest
from .scalars import JSONObject
from .utils import get_manifest


def get_manifest_metadata() -> ManifestMetadata:
    return ManifestMetadata.from_pydantic(
        get_manifest().metadata,
    )


@strawberry.experimental.pydantic.type(model=manifest.ManifestMetadata)
class ManifestMetadata:
    dbt_schema_version: strawberry.auto
    dbt_version: strawberry.auto
    generated_at: strawberry.auto
    invocation_id: strawberry.auto
    env: Optional[JSONObject]
    project_id: strawberry.auto
    user_id: strawberry.auto
    send_anonymous_usage_stats: strawberry.auto
    adapter_type: Optional[str] = strawberry.auto


@strawberry.interface
class NodeInterface:
    manifest_metadata: ManifestMetadata = strawberry.field(
        description="The manifest metadata associated with this node",
        resolver=get_manifest_metadata,
    )
    resource_type: Optional[ResourceType] = strawberry.field(
        description="The resource type of this node"
    )
    name: Optional[str] = strawberry.field(
        description="The user-supplied name of this particular node"
    )
    description: Optional[str] = strawberry.field(
        description="The user-supplied description for this node"
    )
    meta: Optional[JSONObject] = strawberry.field(
        description="The key-value store containing metadata relevant to this node"
    )
    tags: Optional[list[str]] = strawberry.field(
        description="The tags associated with this node"
    )
