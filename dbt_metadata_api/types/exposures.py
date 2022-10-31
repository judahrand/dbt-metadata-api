from typing import Optional
from pydantic import BaseModel

import strawberry

from ..interfaces import NodeInterface
from ..scalars import DateTime
from .models import ModelNode
from .sources import SourceNode
from .utils import convert_to_strawberry, flatten_depends_on


@strawberry.type
class ExposureNode(NodeInterface):

    @property
    def node(self) -> BaseModel:
        return self.manifest.exposures[self.unique_id]

    @strawberry.field
    def depends_on(self) -> Optional[list[str]]:
        return flatten_depends_on(self.node.depends_on)

    @strawberry.field
    def exposure_type(self) -> Optional[str]:
        return self.node.type.value

    @strawberry.field
    def manifest_generated(self) -> Optional[DateTime]:
        return DateTime(self.manifest.metadata.generated_at)

    @strawberry.field
    def maturity(self) -> Optional[str]:
        return self.node.maturity.value

    @strawberry.field
    def owner_email(self) -> Optional[str]:
        return self.node.owner.email

    @strawberry.field
    def owner_name(self) -> Optional[str]:
        return self.node.owner.name

    @strawberry.field
    def parents(self) -> Optional[list[NodeInterface]]:
        return [
            convert_to_strawberry(self.manifest.nodes[unique_id], self.manifest)
            for unique_id in self.manifest.parent_map[self.unique_id]
        ]

    @strawberry.field
    def parents_models(self) -> Optional[list[ModelNode]]:
        return [
            node for node in self.parents() if isinstance(node.resource_type, ModelNode)
        ]

    @strawberry.field
    def parents_sources(self) -> Optional[list[SourceNode]]:
        return [
            node for node in self.parents if isinstance(node.resource_type, SourceNode)
        ]

    @strawberry.field
    def url(self) -> Optional[str]:
        return self.node.url
