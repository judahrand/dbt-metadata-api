from typing import Optional, Union

import strawberry
from dbt.contracts.graph.compiled import (
    CompiledGenericTestNode,
    CompiledSingularTestNode,
)
from dbt.contracts.graph.parsed import ParsedGenericTestNode, ParsedSingularTestNode

from dbt_metadata_api.interfaces import NodeInterface, dbtCoreInterface
from dbt_metadata_api.utils import get_manifest


@strawberry.type
class TestNode(NodeInterface, dbtCoreInterface):
    def get_node(
        self,
        info: strawberry.types.Info,
    ) -> Union[
        ParsedSingularTestNode,
        ParsedGenericTestNode,
        CompiledSingularTestNode,
        CompiledGenericTestNode,
    ]:
        node = get_manifest(info).nodes[self.unique_id]
        if not isinstance(
            node,
            (
                ParsedSingularTestNode,
                ParsedGenericTestNode,
                CompiledSingularTestNode,
                CompiledGenericTestNode,
            ),
        ):
            raise ValueError(f"Node with unique_id={self.unique_id} is not a TestNode")
        return node

    @strawberry.field
    def column_name(self, info: strawberry.types.Info) -> Optional[str]:
        return getattr(self.get_node(info), "column_name", None)

    @strawberry.field
    def compiled_code(self, info: strawberry.types.Info) -> Optional[str]:
        node = self.get_node(info)
        if isinstance(node, (CompiledGenericTestNode, CompiledSingularTestNode)):
            return node.compiled_code
        return None

    @strawberry.field
    def compiled_sql(self, info: strawberry.types.Info) -> Optional[str]:
        if self.get_node(info).language == "sql":
            return self.compiled_code(info)
        return None

    @strawberry.field
    def depends_on(self, info: strawberry.types.Info) -> Optional[list[str]]:
        return self.get_node(info).depends_on_nodes

    @strawberry.field
    def raw_code(self, info: strawberry.types.Info) -> Optional[str]:
        return self.get_node(info).raw_code

    @strawberry.field
    def raw_sql(self, info: strawberry.types.Info) -> Optional[str]:
        if self.get_node(info).language == "sql":
            return self.raw_code(info)
        return None
