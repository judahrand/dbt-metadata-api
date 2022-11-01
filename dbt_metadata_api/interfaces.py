from typing import Optional

import strawberry
import strawberry.types
from dbt.contracts.graph.manifest import WritableManifest
from pydantic import BaseModel

from .scalars import DateTime, JSONObject
from .utils import get_manifest


@strawberry.interface(description="The manifest metadata associated with this node")
class dbtCoreInterface:
    @strawberry.field
    def dbt_schema_version(self, info: strawberry.types.Info) -> str:
        return get_manifest(info.context).metadata.dbt_schema_version

    @strawberry.field
    def dbt_version(self, info: strawberry.types.Info) -> str:
        return get_manifest(info.context).metadata.dbt_version

    @strawberry.field
    def generated_at(self, info: strawberry.types.Info) -> DateTime:
        return DateTime(get_manifest(info.context).metadata.generated_at)

    @strawberry.field
    def invocation_id(self, info: strawberry.types.Info) -> str:
        return get_manifest(info.context).metadata.invocation_id

    @strawberry.field
    def env(self, info: strawberry.types.Info) -> Optional[JSONObject]:
        return JSONObject(get_manifest(info.context).metadata.env)

    @strawberry.field
    def project_id(self, info: strawberry.types.Info) -> Optional[str]:
        return get_manifest(info.context).metadata.project_id

    @strawberry.field
    def user_id(self, info: strawberry.types.Info) -> Optional[str]:
        return get_manifest(info.context).metadata.user_id

    @strawberry.field
    def send_anonymous_usage_stats(self, info: strawberry.types.Info) -> Optional[bool]:
        return get_manifest(info.context).metadata.send_anonymous_usage_stats

    @strawberry.field
    def adapter_type(self, info: strawberry.types.Info) -> Optional[str]:
        return get_manifest(info.context).metadata.adapter_type


@strawberry.interface
class NodeInterface:
    _resource_type: strawberry.Private[str]

    unique_id: str = strawberry.field(
        description="The unique id name of this particular node"
    )

    def get_node(self, manifest: WritableManifest) -> BaseModel:
        node = manifest.nodes[self.unique_id]
        if node.resource_type.name != self._resource_type:
            raise TypeError(f"That unique_id is not a {self._resource_type}.")
        return node

    @strawberry.field(description="The resource type of this node")
    def resource_type(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).resource_type.name

    @strawberry.field(description="The package name of this node")
    def package_name(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).package_name

    @strawberry.field(
        description="The user-supplied name of this particular node",
    )
    def name(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).name

    @strawberry.field(
        description='Relative file path of this resource\'s definition within its "resource path"',
    )
    def path(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).path

    @strawberry.field(
        description="Relative file path of this resource's definition, including its resource path.",
    )
    def original_file_path(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).original_file_path

    @strawberry.field(
        description="The user-supplied description for this node",
    )
    def description(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).description

    @strawberry.field(
        description="The key-value store containing metadata relevant to this node",
    )
    def meta(self, info: strawberry.types.Info) -> Optional[JSONObject]:
        return self.get_node(get_manifest(info.context)).meta

    @strawberry.field(
        description="The tags associated with this node",
    )
    def tags(self, info: strawberry.types.Info) -> Optional[list[str]]:
        return self.get_node(get_manifest(info.context)).tags
