from typing import Optional

from pydantic import BaseModel


def flatten_depends_on(depends_on: BaseModel) -> Optional[list[str]]:
    depends_on = []
    if isinstance(depends_on.macros, str):
        depends_on.append(depends_on.macros)
    else:
        depends_on.extend(depends_on.macros)

    if isinstance(depends_on.nodes, str):
        depends_on.append(depends_on.nodes)
    else:
        depends_on.extend(depends_on.nodes)
        return depends_on
