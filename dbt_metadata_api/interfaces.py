from typing import Optional

import strawberry

from .enums import ResourceType
from .scalars import Datetime, JSONObject
from .utils import get_manifest


@strawberry.interface(description="The manifest metadata associated with this node")
class dbtCoreInterface:
    @strawberry.field
    def dbt_schema_version(self) -> str:
        return get_manifest().metadata.dbt_schema_version

    @strawberry.field
    def dbt_version(self) -> str:
        return get_manifest().metadata.dbt_version

    @strawberry.field
    def generated_at(self) -> Datetime:
        return Datetime(get_manifest().metadata.generated_at)

    @strawberry.field
    def invocation_id(self) -> str:
        return get_manifest().metadata.invocation_id

    @strawberry.field
    def env(self) -> Optional[JSONObject]:
        return JSONObject(get_manifest().metadata.env)

    @strawberry.field
    def project_id(self) -> Optional[str]:
        return get_manifest().metadata.project_id

    @strawberry.field
    def user_id(self) -> Optional[str]:
        return get_manifest().metadata.user_id

    @strawberry.field
    def send_anonymous_usage_stats(self) -> Optional[bool]:
        return get_manifest().metadata.send_anonymous_usage_stats

    @strawberry.field
    def adapter_type(self) -> Optional[str]:
        return get_manifest().metadata.adapter_type


@strawberry.interface
class NodeInterface:
    unique_id: str = strawberry.field(
        description="The unique id name of this particular node"
    )
    resource_type: Optional[ResourceType] = strawberry.field(
        description="The resource type of this node"
    )
    package_name: Optional[ResourceType] = strawberry.field(
        description="The package name of this node"
    )
    name: Optional[str] = strawberry.field(
        description="The user-supplied name of this particular node",
    )
    path: Optional[str] = strawberry.field(
        description='Relative file path of this resource\'s definition within its "resource path"',
    )
    original_file_path: Optional[str] = strawberry.field(
        description="Relative file path of this resource's definition, including its resource path.",
    )
    description: Optional[str] = strawberry.field(
        description="The user-supplied description for this node",
    )
    meta: Optional[JSONObject] = strawberry.field(
        description="The key-value store containing metadata relevant to this node",
    )
    tags: Optional[list[str]] = strawberry.field(
        description="The tags associated with this node",
    )
