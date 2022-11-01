from datetime import datetime
from typing import Any, Optional

import strawberry
import strawberry.types

from .scalars import JSONObject
from .utils import get_manifest


@strawberry.interface(description="The manifest metadata associated with this node")
class dbtCoreInterface:
    @strawberry.field
    def dbt_schema_version(self, info: strawberry.types.Info) -> str:
        return get_manifest(info).metadata.dbt_schema_version

    @strawberry.field
    def dbt_version(self, info: strawberry.types.Info) -> str:
        return get_manifest(info).metadata.dbt_version

    @strawberry.field
    def generated_at(self, info: strawberry.types.Info) -> datetime:
        return get_manifest(info).metadata.generated_at

    @strawberry.field
    def invocation_id(self, info: strawberry.types.Info) -> str:
        return get_manifest(info).metadata.invocation_id

    @strawberry.field
    def env(self, info: strawberry.types.Info) -> Optional[JSONObject]:
        return JSONObject(get_manifest(info).metadata.env)

    @strawberry.field
    def project_id(self, info: strawberry.types.Info) -> Optional[str]:
        return get_manifest(info).metadata.project_id

    @strawberry.field
    def user_id(self, info: strawberry.types.Info) -> Optional[str]:
        return get_manifest(info).metadata.user_id

    @strawberry.field
    def send_anonymous_usage_stats(self, info: strawberry.types.Info) -> Optional[bool]:
        return get_manifest(info).metadata.send_anonymous_usage_stats

    @strawberry.field
    def adapter_type(self, info: strawberry.types.Info) -> Optional[str]:
        return get_manifest(info).metadata.adapter_type


@strawberry.interface
class NodeInterface:
    def get_node(self, info: strawberry.types.Info) -> Any:
        raise NotImplementedError()

    unique_id: str = strawberry.field(
        description="The unique id name of this particular node"
    )

    @strawberry.field(description="The resource type of this node")
    def resource_type(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).resource_type

    @strawberry.field(description="The package name of this node")
    def package_name(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).package_name

    @strawberry.field(
        description="The user-supplied name of this particular node",
    )
    def name(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).name

    @strawberry.field(
        description=(
            "Relative file path of this resource's definition within "
            'its "resource path"'
        ),
    )
    def path(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).path

    @strawberry.field(
        description=(
            "Relative file path of this resource's definition, including "
            "its resource path."
        ),
    )
    def original_file_path(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).original_file_path

    @strawberry.field(
        description="The user-supplied description for this node",
    )
    def description(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).description

    @strawberry.field(
        description="The key-value store containing metadata relevant to this node",
    )
    def meta(self, info: strawberry.types.Info) -> Optional[JSONObject]:
        return self.get_node(info).meta

    @strawberry.field(
        description="The tags associated with this node",
    )
    def tags(self, info: strawberry.types.Info) -> Optional[list[str]]:
        return self.get_node(info).tags
