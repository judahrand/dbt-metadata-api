from typing import Optional

import strawberry

from ..interfaces import NodeInterface


@strawberry.type
class MacroNode(NodeInterface):
    depends_on: Optional[list[str]]
    macro_sql: Optional[str]
    original_file_path: Optional[str]
    path: Optional[str]
    root_path: Optional[str]
