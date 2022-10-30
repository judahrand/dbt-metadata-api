from datetime import datetime
from typing import Any, NewType

import dateutil.parser
import strawberry

AnyScalar = strawberry.scalar(
    NewType("AnyScalar", Any),
    description=(
        "This type can represent any scalar type such as int, float, "
        "string or boolean."
    ),
    serialize=lambda v: v,
    parse_value=lambda v: v,
)

DateTime = strawberry.scalar(
    NewType("DateTime", datetime),
    description=(
        "A date-time string at UTC, such as 2007-12-03T10:15:30Z, compliant with the "
        "`date-time` format outlined in section 5.6 of the RFC 3339 profile of the "
        "ISO 8601 standard for representation of dates and times using the Gregorian "
        "calendar."
    ),
    serialize=lambda v: v.isoformat(),
    parse_value=dateutil.parser.isoparse,
)

JSONObject = strawberry.scalar(
    NewType("JSONObject", dict[str, Any]),
    description=(
        "The `JSONObject` scalar type represents JSON objects as specified by "
        "[ECMA-404]"
        "(http://www.ecma-international.org/publications/files/ECMA-ST/ECMA-404.pdf)."
    ),
    specified_by_url=(
        "http://www.ecma-international.org/publications/files/ECMA-ST/ECMA-404.pdf"
    ),
    serialize=lambda v: v,
    parse_value=lambda v: v,
)
