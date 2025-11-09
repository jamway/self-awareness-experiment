# Self-Aware Code Agent Project

A code-aware agent project designed to understand and analyze its own code during execution.

## Project Setup with uv

1. **Install uv** (if not already installed)
    ```bash
    pip install uv
    ```

2. **Initialize environment**
    ```bash
    uv venv
    ```

3. **Activate environment**
    - Windows:
      ```bash
      .venv/Scripts/activate
      ```
    - Unix/MacOS:
      ```bash
      source .venv/bin/activate
      ```

4. **Install dependencies**
    ```bash
    uv pip install .
    ```

## Project Purpose

This project implements a self-aware code agent that:
- Analyzes its own source code during runtime
- Understands its internal structure and functionality
- Can inspect and reason about its own implementation
- Provides insights into its own decision-making process
- Enables introspective capabilities for AI systems

The agent serves as a demonstration of meta-programming and self-referential AI systems, allowing the code to be aware of its own implementation and behavior patterns.
