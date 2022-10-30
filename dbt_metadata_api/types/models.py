from typing import Optional

import strawberry

from ..interfaces import NodeInterface
from .common import CatalogColumn
from .sources import SourceNode


@strawberry.type
class ModelNode(NodeInterface):
    alias: Optional[str]
    args: Optional[strawberry.scalars.JSON]
    children_l1: Optional[list[str]]
    columns: Optional[CatalogColumn]
    comment: Optional[str]
    compiled_code: Optional[str]
    compiled_sql: Optional[str]
    database: Optional[str]
    depends_on: Optional[list[str]]
    description: Optional[str]
    materialized_type: Optional[str]
    owner: Optional[str]
    parents_models: Optional["ModelNode"]
    parents_sources: Optional[SourceNode]
    raw_code: Optional[str]
    raw_sql: Optional[str]
    schema: Optional[str]
    type: Optional[str]
