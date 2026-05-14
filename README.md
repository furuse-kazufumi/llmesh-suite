# llmesh-suite

**One-shot installer for the llmesh family.**

```bash
pip install llmesh-suite
```

Pulls in three sibling projects in a single command:

| Package | Role | Repo |
|---------|------|------|
| [`llmesh-mcp`](https://pypi.org/project/llmesh-mcp/)   | Multi-protocol LLM gateway (Modbus / OPC-UA / MQTT / HTTP / SSH / Email / RAG / Audit / SPC) | https://github.com/furuse-kazufumi/llmesh |
| [`llmesh-llove`](https://pypi.org/project/llmesh-llove/) | Terminal-first dashboard (SensorEvent / SPC / RAG / Audit + games & demos) | https://github.com/furuse-kazufumi/llove |
| [`llmesh-llive`](https://pypi.org/project/llmesh-llive/) | Self-evolving modular-memory LLM (4-layer external memory + formal verification + TRIZ self-evolution + Rust hot-path) | https://github.com/furuse-kazufumi/llive |

This package itself contains **no runtime code** — it is a pure dependency
shim so that users do not have to remember three install names.

## Why a meta-package, not a monorepo?

`llmesh` is designed to run on embedded Linux / RTOS targets with minimal
dependencies, so it cannot pull in `textual` / `rich` / `pillow` (which
`llove` requires for its TUI), nor `torch` / `faiss` / `peft` / `cryptography`
(which `llive` requires for its 4-layer memory + signed adapters). Keeping
the three as separate packages preserves:

* **Independent deployability** — `llmesh-mcp` on the gateway, `llmesh-llove`
  on the operator console, `llmesh-llive` on the GPU node.
* **Independent versioning** — each project follows its own SemVer.
* **Independent test surfaces** — `llove`'s textual-snapshot tests and
  `llive`'s formal-verification suite do not block `llmesh`'s OWASP-clean CI.

A meta-package gives users the "one command, all tools" experience without
forcing the three repositories into a monolith.

## Quick start

```bash
pip install llmesh-suite
llmesh dashboard            # llmesh CLI spawns llove TUI via subprocess
llove demo                  # or run llove directly
```

For the full industrial / vision / RAG stack:

```bash
pip install "llmesh-suite[all]"
```

## Disambiguation

This project is unrelated to [`mesh-llm`](https://github.com/michaelneale/mesh-llm),
which pools GPUs across machines to run a single LLM in distributed inference.
`llmesh-suite` is the I/O / protocol / dashboard side; `mesh-llm` is the
inference-parallelisation side.

## Licence

MIT. See [`LICENSE`](LICENSE).
