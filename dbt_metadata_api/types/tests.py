from typing import Optional

import strawberry

from ..interfaces import NodeInterface, dbtCoreInterface
from .utils import flatten_depends_on


@strawberry.type
class TestNode(NodeInterface, dbtCoreInterface):
    @strawberry.field
    def column_name(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(self.get_node(info.context["manifest"]), "column_name", None)

    @strawberry.field
    def compiled_code(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(self.get_node(info.context["manifest"]), "compiled_code", None)

    @strawberry.field
    def compiled_sql(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(self.get_node(info.context["manifest"]), "compiled_sql", None)

    @strawberry.field
    def depends_on(self, info: strawberry.types.Info) -> Optional[list[str]]:
        return flatten_depends_on(self.get_node(info.context["manifest"]).depends_on)

    @strawberry.field
    def raw_code(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(self.get_node(info.context["manifest"]), "raw_code", None)

    @strawberry.field
    def raw_sql(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(self.get_node(info.context["manifest"]), "raw_sql", None)
