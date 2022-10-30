from typing import Optional

import strawberry

from ..interfaces import NodeInterface


@strawberry.type
class TestNode(NodeInterface):
    column_name: Optional[str]
    compiled_code: Optional[str]
    compiled_sql: Optional[str]
    depends_on: Optional[list[str]]
    fail: Optional[bool]
    raw_code: Optional[str]
    raw_sql: Optional[str]
    skip: Optional[bool]
    state: Optional[str]
    status: Optional[str]
    warn: Optional[bool]
