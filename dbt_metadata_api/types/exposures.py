from typing import Optional

import strawberry
from dbt.contracts.graph.manifest import WritableManifest
from pydantic import BaseModel

from ..interfaces import NodeInterface, dbtCoreInterface
from ..scalars import DateTime
from ..utils import get_manifest
from .models import ModelNode
from .sources import SourceNode
from .utils import convert_to_strawberry, flatten_depends_on


@strawberry.type
class ExposureNode(NodeInterface, dbtCoreInterface):
    _resource_type: strawberry.Private[str] = "exposure"

    def get_node(self, manifest: WritableManifest) -> BaseModel:
        return manifest.exposures[self.unique_id]

    @strawberry.field
    def depends_on(self, info: strawberry.types.Info) -> Optional[list[str]]:
        return flatten_depends_on(self.get_node(get_manifest(info.context)).depends_on)

    @strawberry.field
    def exposure_type(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).type.value

    @strawberry.field
    def manifest_generated(self, info: strawberry.types.Info) -> Optional[DateTime]:
        return DateTime(get_manifest(info.context).metadata.generated_at)

    @strawberry.field
    def maturity(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).maturity.value

    @strawberry.field
    def owner_email(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).owner.email

    @strawberry.field
    def owner_name(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).owner.name

    @strawberry.field
    def parents(self, info: strawberry.types.Info) -> Optional[list[NodeInterface]]:
        manifest = get_manifest(info.context)
        return [
            convert_to_strawberry(
                unique_id, manifest.nodes[unique_id].resource_type.name
            )
            for unique_id in manifest.parent_map[self.unique_id]
        ]

    @strawberry.field
    def parents_models(self, info: strawberry.types.Info) -> Optional[list[ModelNode]]:
        return [
            node for node in self.parents() if isinstance(node.resource_type, ModelNode)
        ]

    @strawberry.field
    def parents_sources(
        self, info: strawberry.types.Info
    ) -> Optional[list[SourceNode]]:
        return [
            node for node in self.parents if isinstance(node.resource_type, SourceNode)
        ]

    @strawberry.field
    def url(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).url
