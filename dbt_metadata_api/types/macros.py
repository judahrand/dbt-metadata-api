from typing import Optional
from pydantic import BaseModel

import strawberry

from ..interfaces import NodeInterface
from .utils import flatten_depends_on


@strawberry.type
class MacroNode(NodeInterface):

    @property
    def node(self) -> BaseModel:
        return self.manifest.macros[self.unique_id]

    @strawberry.field
    def depends_on(self) -> Optional[list[str]]:
        return flatten_depends_on(self.node.depends_on)

    @strawberry.field
    def macro_sql(self) -> Optional[str]:
        return self.node.macro_sql

    @strawberry.field
    def original_file_path(self) -> Optional[str]:
        return self.node.original_file_path

    @strawberry.field
    def path(self) -> Optional[str]:
        return self.node.path

    @strawberry.field
    def root_path(self) -> Optional[str]:
        return self.node.root_path
