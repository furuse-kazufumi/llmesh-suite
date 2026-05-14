"""llmesh-suite — meta-package marker.

This package intentionally contains no runtime code. It exists only so that
the wheel builder produces a wheel with at least one Python module. The real
work is done by the three dependencies declared in ``pyproject.toml``:

* ``llmesh-mcp``   — multi-protocol LLM gateway (backend)
* ``llmesh-llove`` — terminal-first dashboard (frontend)
* ``llmesh-llive`` — self-evolving modular-memory LLM (4-layer memory + formal
  verification + TRIZ self-evolution + Rust hot-path)

Install via ``pip install llmesh-suite`` to get all three at once, then run::

    llmesh dashboard            # launches llove TUI through llmesh CLI
    llove demo                  # or call llove directly
    llive --help                # llive CLI for memory / evolution / triz
"""

__version__ = "0.2.1"
