from typing import Optional

import strawberry

from ..interfaces import NodeInterface, dbtCoreInterface
from .common import CatalogColumn, CatalogStat


@strawberry.type
class SeedNode(NodeInterface, dbtCoreInterface):
    alias: Optional[str]
    children_l1: Optional[str]
    columns: Optional[CatalogColumn]
    comment: Optional[str]
    compiled_code: Optional[str]
    compiled_sql: Optional[str]
    database: Optional[str]
    owner: Optional[str]
    raw_code: Optional[str]
    raw_sql: Optional[str]
    schema: Optional[str]
    skip: Optional[bool]
    stats: Optional[list[CatalogStat]]
    status: Optional[str]
    type: Optional[str]
