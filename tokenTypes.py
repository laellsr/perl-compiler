from enum import Enum


class TokenCategory(Enum):
    SIGIL_ARRAY = 1
    SIGIL_SCALAR_INDEX = 2
    SIGIL_GLOB = 3
    SIGIL_HASH = 4
    SIGIL_CODE = 5
