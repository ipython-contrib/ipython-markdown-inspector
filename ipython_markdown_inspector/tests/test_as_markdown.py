from IPython.core.interactiveshell import InteractiveShell
from IPython.core.oinspect import InspectorHookData
from IPython import get_ipython
import pytest

from ipython_markdown_inspector.formatter import as_markdown


def simple_func(arg):
    """Calls :py:func:`bool` on ``arg``"""
    return bool(arg)


class SimpleClass:
    pass


@pytest.mark.parametrize(
    "object_name, part",
    [
        ["%%python", "Run cells with python"],
        ["simple_func", "Calls `bool` on ``arg``"],
        ["simple_func", "| Type | `function` |"],
        ["test_int", "| Type | `int` |"],
        ["test_int", "| String form | `1` |"],
        ["test_str", "| Type | `str` |"],
        ["test_str", "| String form | `a` |"],
        ["test_str", "| Length | `1` |"],
        ["simple_cls", "| Type | `type` |"],
        ["simple_instance", "| Type | `SimpleClass` |"],
    ],
)
def test_result_contains(object_name, part):
    ip: InteractiveShell = get_ipython()  # type: ignore
    ip.user_ns["test_str"] = "a"
    ip.user_ns["test_int"] = 1
    ip.user_ns["simple_func"] = simple_func
    ip.user_ns["simple_cls"] = SimpleClass
    ip.user_ns["simple_instance"] = SimpleClass()
    oinfo = ip._object_find(object_name)
    detail_level = 0
    info_dict = ip.inspector.info(oinfo.obj, object_name)
    data = InspectorHookData(
        obj=oinfo.obj,
        info=oinfo,
        info_dict=info_dict,
        detail_level=detail_level,
        omit_sections=[],
    )
    assert part in as_markdown(data)
