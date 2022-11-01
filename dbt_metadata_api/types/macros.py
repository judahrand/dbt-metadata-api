from typing import Optional

import strawberry
from dbt.contracts.graph.manifest import WritableManifest
from pydantic import BaseModel

from ..interfaces import NodeInterface, dbtCoreInterface
from ..utils import get_manifest
from .utils import flatten_depends_on


@strawberry.type
class MacroNode(NodeInterface, dbtCoreInterface):
    _resource_type: strawberry.Private[str] = "macro"

    def get_node(self, manifest: WritableManifest) -> BaseModel:
        node = manifest.macros[self.unique_id]

    @strawberry.field
    def depends_on(self, info: strawberry.types.Info) -> Optional[list[str]]:
        return flatten_depends_on(self.get_node(get_manifest(info.context)).depends_on)

    @strawberry.field
    def macro_sql(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).macro_sql

    @strawberry.field
    def original_file_path(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).original_file_path

    @strawberry.field
    def path(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).path

    @strawberry.field
    def root_path(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(get_manifest(info.context)).root_path
