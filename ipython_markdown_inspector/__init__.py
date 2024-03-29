from typing import List

from IPython.core.interactiveshell import InteractiveShell

from .formatter import as_markdown


ORIGINAL_HOOK = None


def load_ipython_extension(ipython: InteractiveShell):
    global ORIGINAL_HOOK
    ORIGINAL_HOOK = ipython.inspector.mime_hooks.get("text/markdown", None)
    ipython.inspector.mime_hooks["text/markdown"] = as_markdown


def unload_ipython_extension(ipython: InteractiveShell):
    if ORIGINAL_HOOK is None:
        del ipython.inspector.mime_hooks["text/markdown"]
    else:
        ipython.inspector.mime_hooks["text/markdown"] = ORIGINAL_HOOK


__all__: List[str] = []
