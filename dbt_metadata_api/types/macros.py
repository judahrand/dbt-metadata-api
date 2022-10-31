from typing import Optional

import strawberry
from pydantic import BaseModel

from ..interfaces import NodeInterface, dbtCoreInterface
from ..utils import Manifest
from .utils import flatten_depends_on


@strawberry.type
class MacroNode(NodeInterface, dbtCoreInterface):
    _resource_type: strawberry.Private[str] = "macro"

    def get_node(self, manifest: Manifest) -> BaseModel:
        node = manifest.macros[self.unique_id]

    @strawberry.field
    def depends_on(self, info: strawberry.types.Info) -> Optional[list[str]]:
        return flatten_depends_on(self.get_node(info.context["manifest"]).depends_on)

    @strawberry.field
    def macro_sql(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info.context["manifest"]).macro_sql

    @strawberry.field
    def original_file_path(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info.context["manifest"]).original_file_path

    @strawberry.field
    def path(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info.context["manifest"]).path

    @strawberry.field
    def root_path(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info.context["manifest"]).root_path
