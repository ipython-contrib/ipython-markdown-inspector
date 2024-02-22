# ipython-markdown-inspector

[![tests](https://github.com/ipython-contrib/ipython-markdown-inspector/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/ipython-contrib/ipython-markdown-inspector/actions/workflows/tests.yml)
![CodeQL](https://github.com/ipython-contrib/ipython-markdown-inspector/workflows/CodeQL/badge.svg)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ipython-contrib/ipython-markdown-inspector/main?urlpath=lab)
[![pypi-version](https://img.shields.io/pypi/v/ipython-markdown-inspector.svg)](https://python.org/pypi/ipython-markdown-inspector)

IPython extension providing inspection results as Markdown, enabling better integration with Jupyter Notebook and JupyterLab.
Depends on [`docstring-to-markdown`](https://github.com/python-lsp/docstring-to-markdown).

![](https://raw.githubusercontent.com/ipython-contrib/ipython-markdown-inspector/main/docs/demo.png)

## Installation

Requires `IPython` 8.22 or newer (which requires Python 3.10 or newer).

```bash
pip install ipython-markdown-inspector
```

## Usage

To load an extension while IPython is running, use the `%load_ext` magic:

```ipython
%load_ext ipython_markdown_inspector
```

To load it each time IPython starts, list it in your [configuration file](https://ipython.readthedocs.io/en/stable/config/intro.html):

```python
c.InteractiveShellApp.extensions = [
    'ipython_markdown_inspector'
]
```

After enabling the extension, both the contents of "Contextual Help" panel,
and results of info requests such as `%run?` or `df?` will provide the output in Markdown format.
