from typing import Optional

import strawberry
import strawberry.types
from dbt.contracts.graph.parsed import ParsedMacro

from ..interfaces import NodeInterface, dbtCoreInterface
from ..utils import get_manifest


@strawberry.type
class MacroNode(NodeInterface, dbtCoreInterface):
    def get_node(self, info: strawberry.types.Info) -> ParsedMacro:
        return get_manifest(info).macros[self.unique_id]

    @strawberry.field
    def depends_on(self, info: strawberry.types.Info) -> Optional[list[str]]:
        return self.get_node(info).depends_on.macros

    @strawberry.field
    def macro_sql(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).macro_sql

    @strawberry.field
    def original_file_path(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).original_file_path

    @strawberry.field
    def path(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).path

    @strawberry.field
    def root_path(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).root_path
