import enum

import strawberry


@strawberry.enum
class FreshnessStatus(enum.Enum):
    error = "error"
    pass_ = "pass"
    warn = "warn"


@strawberry.enum
class TimePeriod(enum.Enum):
    day = "day"
    hour = "hour"
    minute = "minute"
