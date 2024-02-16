from dataclasses import dataclass
from typing import Literal


@dataclass
class Field:
    key: str
    label: str
    kind: str
    min_level: int = 0


@dataclass
class RowField(Field):
    kind: Literal["row"] = "row"


@dataclass
class CodeField(Field):
    kind: Literal["code"] = "code"


@dataclass
class DocField(Field):
    kind: Literal["doc"] = "doc"
