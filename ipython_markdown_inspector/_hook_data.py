try:
    from IPython.core.oinspect import InspectorHookData  # type: ignore
except ImportError:
    # TODO: remove once we require a version which includes
    # https://github.com/ipython/ipython/pull/14342
    from ._ipython_patch import InspectorHookData


__all__ = ["InspectorHookData"]
