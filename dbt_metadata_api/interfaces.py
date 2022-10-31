from typing import Optional

import strawberry
import strawberry.types
from pydantic import BaseModel

from .scalars import DateTime, JSONObject


@strawberry.interface(description="The manifest metadata associated with this node")
class dbtCoreInterface:
    manifest: strawberry.Private[BaseModel]

    @strawberry.field
    def dbt_schema_version(self, info: strawberry.types.Info) -> str:
        return info.context["manifest"].metadata.dbt_schema_version

    @strawberry.field
    def dbt_version(self, info: strawberry.types.Info) -> str:
        return info.context["manifest"].metadata.dbt_version

    @strawberry.field
    def generated_at(self, info: strawberry.types.Info) -> DateTime:
        return DateTime(info.context["manifest"].metadata.generated_at)

    @strawberry.field
    def invocation_id(self, info: strawberry.types.Info) -> str:
        return info.context["manifest"].metadata.invocation_id

    @strawberry.field
    def env(self, info: strawberry.types.Info) -> Optional[JSONObject]:
        return JSONObject(info.context["manifest"].metadata.env)

    @strawberry.field
    def project_id(self, info: strawberry.types.Info) -> Optional[str]:
        return info.context["manifest"].metadata.project_id

    @strawberry.field
    def user_id(self, info: strawberry.types.Info) -> Optional[str]:
        return info.context["manifest"].metadata.user_id

    @strawberry.field
    def send_anonymous_usage_stats(self, info: strawberry.types.Info) -> Optional[bool]:
        return info.context["manifest"].metadata.send_anonymous_usage_stats

    @strawberry.field
    def adapter_type(self, info: strawberry.types.Info) -> Optional[str]:
        return info.context["manifest"].metadata.adapter_type


@strawberry.interface
class NodeInterface(dbtCoreInterface):

    unique_id: str = strawberry.field(
        description="The unique id name of this particular node"
    )

    @property
    def node(self) -> BaseModel:
        return self.manifest.nodes[self.unique_id]

    @strawberry.field(description="The resource type of this node")
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
