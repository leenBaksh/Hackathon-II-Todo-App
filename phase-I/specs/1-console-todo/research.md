# Research: Phase I In-Memory Console Todo App

## Decision: Python 3.13+ with UV for Project Management
- **Rationale**: Python 3.13 is the latest stable version providing modern features. UV is the fastest Python package manager and provides reliable environment reproduction.
- **Alternatives considered**: Poetry (slower, more complex), Pipenv (less reliable), standard venv (requires manual management).

## Decision: Interactive REPL using `cmd` module or raw `input()` loop
- **Rationale**: For a Phase I basic console app, a raw `while True` loop with `input()` provides maximum control with zero external dependencies, adhering to the "Tech Stack Fidelity" principle.
- **Alternatives considered**: `cmd` module (more structured but slightly more overhead), `argparse` (better for one-off commands, less suited for interactive sessions).

## Decision: Simple Dataclass for Task Model
- **Rationale**: Dataclasses provide a clean, type-hinted way to define data structures without the overhead of more complex libraries like Pydantic (which is reserved for Phase II).
- **Alternatives considered**: Plain dictionaries (less type safety), namedtuples (immutable, making updates awkward).

## Decision: Manual Command Parsing
- **Rationale**: Commands are simple (e.g., `add "Buy Milk"`). A split-based parser is sufficient and avoids external dependencies like `click` or `typer` in Phase I.
- **Alternatives considered**: `shlex` for better quote handling (will use `shlex.split` for robust parsing).
