"""llmesh-suite — meta-package marker.

This package intentionally contains no runtime code. It exists only so that
the wheel builder produces a wheel with at least one Python module. The real
work is done by the two dependencies declared in ``pyproject.toml``:

* ``llmesh-mcp``   — multi-protocol LLM gateway (backend)
* ``llmesh-llove`` — terminal-first dashboard (frontend)

Install via ``pip install llmesh-suite`` to get both at once, then run::

    llmesh dashboard            # launches llove TUI through llmesh CLI
    llove demo                  # or call llove directly
"""

__version__ = "0.1.0"
