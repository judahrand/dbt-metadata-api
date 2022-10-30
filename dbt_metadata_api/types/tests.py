from typing import Optional

import strawberry

from ..interfaces import NodeInterface
from .utils import flatten_depends_on


@strawberry.type
class TestNode(NodeInterface):
    def __post_init__(self) -> None:
        if self.node.resource_type.value != "test":
            raise TypeError("That unique_id is not a test.")

    @strawberry.field
    def column_name(self) -> Optional[str]:
        return getattr(self.node, "column_name", None)

    @strawberry.field
    def compiled_code(self) -> Optional[str]:
        return self.node.compiled_code

    @strawberry.field
    def compiled_sql(self) -> Optional[str]:
        if getattr(self.node, "language", "sql") == "sql":
            return self.node.compiled_code

    @strawberry.field
    def depends_on(self) -> Optional[list[str]]:
        return flatten_depends_on(self.node.depends_on)

    @strawberry.field
    def raw_code(self) -> Optional[str]:
        return self.node.raw_code

    @strawberry.field
    def raw_sql(self) -> Optional[str]:
        if getattr(self.node, "language", "sql") == "sql":
            return self.node.raw_code
