from typing import Optional

import strawberry

from ..interfaces import NodeInterface
from ..scalars import DateTime
from .models import ModelNode
from .sources import SourceNode


@strawberry.type
class ExposureNode(NodeInterface):
    depends_on: Optional[list[str]]
    exposure_type: Optional[str]
    manifest_generated: Optional[DateTime]
    maturity: Optional[str]
    owner_email: Optional[str]
    owner_name: Optional[str]
    parents: Optional[NodeInterface]
    parents_models: Optional[ModelNode]
    parents_sources: Optional[SourceNode]
    url: Optional[str]
