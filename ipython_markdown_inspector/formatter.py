from typing import cast, Dict, List

import docstring_to_markdown
from IPython.core.oinspect import is_simple_callable, InspectorHookData

from .models import Field, CodeField, DocField, RowField


FIELDS: Dict[str, List[Field]] = {
    "alias": [
        CodeField(label="Repr", key="string_form"),
    ],
    "magic": [
        DocField(label="Docstring", key="docstring"),
        CodeField(label="Source", key="source", min_level=1),
        RowField(label="File", key="file"),
    ],
    "class_or_callable": [
        # Functions, methods, classes
        CodeField(label="Signature", key="definition"),
        CodeField(label="Init signature", key="init_definition"),
        DocField(label="Docstring", key="docstring"),
        CodeField(label="Source", key="source", min_level=1),
        DocField(label="Init docstring", key="init_docstring"),
        RowField(label="File", key="file"),
        RowField(label="Type", key="type_name"),
        RowField(label="Subclasses", key="subclasses"),
    ],
    "default": [
        # General Python objects
        CodeField(label="Signature", key="definition"),
        CodeField(label="Call signature", key="call_def"),
        RowField(label="Type", key="type_name"),
        RowField(label="String form", key="string_form"),
        RowField(label="Namespace", key="namespace"),
        RowField(label="Length", key="length"),
        RowField(label="File", key="file"),
        DocField(label="Docstring", key="docstring"),
        CodeField(label="Source", key="source", min_level=1),
        DocField(label="Class docstring", key="class_docstring"),
        DocField(label="Init docstring", key="init_docstring"),
        DocField(label="Call docstring", key="call_docstring"),
    ],
}


TABLE_STARTER = """\
| <!-- --> | <!-- --> |
|----------|----------|\
"""


def markdown_formatter(text: str) -> str:
    try:
        converted = docstring_to_markdown.convert(text)
        return converted
    except docstring_to_markdown.UnknownFormatError:
        return f"<pre>{text}</pre>"


def code_formatter(code: str, language="python") -> str:
    return f"```{language}\n{code}\n```"


def as_markdown(data: InspectorHookData) -> str:
    if data.info and not data.info.found:
        return str(data.info)

    info_dict = data.info_dict

    if info_dict["namespace"] == "Interactive":
        info_dict["namespace"] = None

    # TODO: maybe remove docstring from source?
    # info_dict["source"] = remove_docstring(source)

    if info_dict["isalias"]:
        fields = FIELDS["alias"]
    elif info_dict["ismagic"]:
        fields = FIELDS["magic"]
    if info_dict["isclass"] or is_simple_callable(data.obj):
        fields = FIELDS["class_or_callable"]
    else:
        fields = FIELDS["default"]

    chunks = []

    in_table = False
    for field in fields:
        value = info_dict.get(field.key)
        if value is None:
            continue
        if field.kind == "row":
            if not in_table:
                in_table = True
                chunks.append(TABLE_STARTER)
            chunks[-1] += f"\n| {field.label} | `{value}` |"
        if field.kind == "code":
            chunks.append(f"#### {field.label}\n\n" + code_formatter(cast(str, value)))
        if field.kind == "doc":
            chunks.append(
                f"#### {field.label}\n\n" + markdown_formatter(cast(str, value))
            )

    return "\n\n".join(chunks)
