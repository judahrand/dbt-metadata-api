from typing import Optional

import strawberry

from dbt_metadata_api.scalars import AnyScalar, JSONObject

from ..enums import TimePeriod


@strawberry.type
class CatalogColumn:
    description: Optional[str]
    index: Optional[int]
    meta: Optional[JSONObject]
    name: Optional[str]
    tags: Optional[list[str]]
    type: Optional[str]


@strawberry.type
class CatalogStat:
    description: Optional[str]
    id: Optional[str]
    include: Optional[bool]
    label: Optional[str]
    value: Optional[AnyScalar]


@strawberry.type
class Criteria:
    error_after: Optional["CriteriaInfo"]
    warn_after: Optional["CriteriaInfo"]


@strawberry.type
class CriteriaInfo:
    count: Optional[int]
    period: Optional[TimePeriod]
