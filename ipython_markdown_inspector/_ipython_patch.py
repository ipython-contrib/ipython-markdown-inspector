from typing import Any, TypedDict, Optional
from dataclasses import dataclass

from IPython.core.oinspect import OInfo


class InfoDict(TypedDict):
    type_name: Optional[str]
    base_class: Optional[str]
    string_form: Optional[str]
    namespace: Optional[str]
    length: Optional[str]
    file: Optional[str]
    definition: Optional[str]
    docstring: Optional[str]
    source: Optional[str]
    init_definition: Optional[str]
    class_docstring: Optional[str]
    init_docstring: Optional[str]
    call_def: Optional[str]
    call_docstring: Optional[str]
    subclasses: Optional[str]
    # These won't be printed but will be used to determine how to
    # format the object
    ismagic: bool
    isalias: bool
    isclass: bool
    found: bool
    name: str


@dataclass
class InspectorHookData:
    """Data passed to the mime hook"""

    obj: Any
    info: Optional[OInfo]
    info_dict: InfoDict
    detail_level: int
    omit_sections: list[str]
