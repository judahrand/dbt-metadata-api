from typing import Optional

import strawberry

from ..enums import FreshnessStatus
from ..interfaces import NodeInterface, dbtCoreInterface
from ..scalars import DateTime
from .common import CatalogColumn, CatalogStat, Criteria
from .tests import TestNode


@strawberry.type
class SourceNode(NodeInterface, dbtCoreInterface):
    children_l1: Optional[list[str]]
    columns: Optional[CatalogColumn]
    comment: Optional[str]
    criteria: Optional[Criteria]
    database: Optional[str]
    freshness_checked: Optional[bool]
    identifier: Optional[str]
    loader: Optional[str]
    max_loaded_at: Optional[DateTime]
    max_loaded_at_time_ago_in_s: Optional[float]
    owner: Optional[str]
    schema: Optional[str]
    snapshotted_at: Optional[str]
    source_description: Optional[str]
    source_name: Optional[str]
    state: Optional[FreshnessStatus]
    stats: Optional[list[CatalogStat]]
    tests: Optional[list[TestNode]]
    type: Optional[str]
