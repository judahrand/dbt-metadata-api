from datetime import datetime
from typing import Annotated, Optional

import strawberry
import strawberry.types
from dbt.contracts.graph.parsed import ParsedExposure

from dbt_metadata_api.interfaces import NodeInterface, dbtCoreInterface
from dbt_metadata_api.utils import get_manifest

from .models import ModelNode
from .sources import SourceNode
from .utils import get_parents


@strawberry.type
class ExposureNode(NodeInterface, dbtCoreInterface):
    def get_node(self, info: strawberry.types.Info) -> ParsedExposure:
        return get_manifest(info).exposures[self.unique_id]

    @strawberry.field
    def depends_on(self, info: strawberry.types.Info) -> Optional[list[str]]:
        return self.get_node(info).depends_on_nodes

    @strawberry.field
    def exposure_type(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).type.value

    @strawberry.field
    def manifest_generated(self, info: strawberry.types.Info) -> Optional[datetime]:
        return get_manifest(info).metadata.generated_at

    @strawberry.field
    def maturity(self, info: strawberry.types.Info) -> Optional[str]:
        node = self.get_node(info)
        if node.maturity is not None:
            return node.maturity.value
        return None

    @strawberry.field
    def owner_email(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).owner.email

    @strawberry.field
    def owner_name(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).owner.name

    @strawberry.field
    def parents_models(
        self, info: strawberry.types.Info
    ) -> Optional[list["ModelNode"]]:
        parents = get_parents(
            self.unique_id, get_manifest(info), resource_types=("source",)
        )
        if parents is not None:
            return [ModelNode(unique_id=unique_id) for unique_id in parents]
        return None

    def parents_sources(
        self, info: strawberry.types.Info
    ) -> Optional[list[Annotated["SourceNode", strawberry.lazy(".sources")]]]:
        parents = get_parents(
            self.unique_id, get_manifest(info), resource_types=("source",)
        )
        if parents is not None:
            return [SourceNode(unique_id=unique_id) for unique_id in parents]
        return None

    @strawberry.field
    def url(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).url
