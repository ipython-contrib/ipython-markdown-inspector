from functools import partial
from typing import Any, List, Optional, Union

from IPython.core.interactiveshell import InteractiveShell
from IPython.core.oinspect import OInfo

from ._hook_data import InspectorHookData
from .formatter import as_markdown


def hook(
    obj_or_data: Union[InspectorHookData, Any],
    info: Optional[OInfo] = None,
    *_,
    ipython: InteractiveShell,
) -> str:
    if isinstance(obj_or_data, InspectorHookData):
        data = obj_or_data
    else:
        # fallback for IPython 8.21
        obj = obj_or_data
        detail_level = 0
        omit_sections: List[str] = []
        info_dict = ipython.inspector.info(
            obj, "", info=info, detail_level=detail_level
        )
        data = InspectorHookData(
            obj=obj,
            info=info,
            info_dict=info_dict,
            detail_level=detail_level,
            omit_sections=omit_sections,
        )
    return as_markdown(data)


ORIGINAL_HOOK = None


def load_ipython_extension(ipython: InteractiveShell):
    global ORIGINAL_HOOK
    ORIGINAL_HOOK = ipython.inspector.mime_hooks.get("text/markdown", None)
    ipython.inspector.mime_hooks["text/markdown"] = partial(hook, ipython=ipython)


def unload_ipython_extension(ipython: InteractiveShell):
    if ORIGINAL_HOOK is None:
        del ipython.inspector.mime_hooks["text/markdown"]
    else:
        ipython.inspector.mime_hooks["text/markdown"] = ORIGINAL_HOOK


__all__: List[str] = []
