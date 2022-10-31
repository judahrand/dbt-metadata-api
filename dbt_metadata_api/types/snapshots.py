from typing import Optional

import strawberry

from ..interfaces import NodeInterface, dbtCoreInterface
from .common import CatalogColumn, CatalogStat
from .models import ModelNode
from .sources import SourceNode


@strawberry.type
class SnapshotNode(NodeInterface, dbtCoreInterface):
    _resource_type: strawberry.Private[str] = "snapshot"

    alias: Optional[str]
    children_l1: Optional[list[str]]
    columns: Optional[list[CatalogColumn]]
    comment: Optional[str]
    compiled_code: Optional[str]
    compiled_sql: Optional[str]
    database: Optional[str]
    owner: Optional[str]
    parents_models: Optional[list[ModelNode]]
    parents_sources: Optional[list[SourceNode]]
    raw_code: Optional[str]
    raw_sql: Optional[str]
    schema: Optional[str]
    skip: Optional[str]
    stats: Optional[list[CatalogStat]]
    status: Optional[str]
    type: Optional[str]
