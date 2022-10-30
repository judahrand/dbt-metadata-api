from typing import Optional

import strawberry

from ..interfaces import NodeInterface


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
        depends_on = []
        if isinstance(self.node.depends_on.macros, str):
            depends_on.append(self.node.depends_on.macros)
        else:
            depends_on.extend(self.node.depends_on.macros)

        if isinstance(self.node.depends_on.nodes, str):
            depends_on.append(self.node.depends_on.nodes)
        else:
            depends_on.extend(self.node.depends_on.nodes)
        return depends_on

    @strawberry.field
    def raw_code(self) -> Optional[str]:
        return self.node.raw_code

    @strawberry.field
    def raw_sql(self) -> Optional[str]:
        if getattr(self.node, "language", "sql") == "sql":
            return self.node.raw_code
