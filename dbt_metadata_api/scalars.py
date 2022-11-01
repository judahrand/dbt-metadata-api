from typing import Any, NewType

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
