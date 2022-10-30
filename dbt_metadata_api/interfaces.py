from typing import Optional
from pydantic import BaseModel

import strawberry

from .scalars import DateTime, JSONObject
from .utils import get_manifest


@strawberry.interface(description="The manifest metadata associated with this node")
class dbtCoreInterface:
    manifest: strawberry.Private[BaseModel]

    @strawberry.field
    def dbt_schema_version(self) -> str:
        return get_manifest().metadata.dbt_schema_version

    @strawberry.field
    def dbt_version(self) -> str:
        return get_manifest().metadata.dbt_version

    @strawberry.field
    def generated_at(self) -> DateTime:
        return DateTime(get_manifest().metadata.generated_at)

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
class NodeInterface(dbtCoreInterface):

    unique_id: str = strawberry.field(
        description="The unique id name of this particular node"
    )

    @property
    def node(self) -> BaseModel:
        return self.manifest.nodes[self.unique_id]

    @strawberry.field(
        description="The resource type of this node"
    )
    def resource_type(self) -> Optional[str]:
        return self.node.resource_type.value

    @strawberry.field(description="The package name of this node")
    def package_name(self) -> Optional[str]:
        return self.node.package_name

    @strawberry.field(
        description="The user-supplied name of this particular node",
    )
    def name(self) -> Optional[str]:
        return self.node.name

    @strawberry.field(
        description='Relative file path of this resource\'s definition within its "resource path"',
    )
    def path(self) -> Optional[str]:
        return self.node.path

    @strawberry.field(
        description="Relative file path of this resource's definition, including its resource path.",
    )
    def original_file_path(self) -> Optional[str]:
        return self.node.original_file_path

    @strawberry.field(
        description="The user-supplied description for this node",
    )
    def description(self) -> Optional[str]:
        return self.node.description

    @strawberry.field(
        description="The key-value store containing metadata relevant to this node",
    )
    def meta(self) -> Optional[JSONObject]:
        return self.node.meta

    @strawberry.field(
        description="The tags associated with this node",
    )
    def tags(self) -> Optional[list[str]]:
        return self.node.tags
