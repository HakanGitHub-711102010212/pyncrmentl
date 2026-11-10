# pyncrmentl

[![PyPI version](https://shields.io)](https://pypi.org)
[![Python versions](https://shields.io)](https://pypi.org)
[![Publish to PyPI](https://github.com)](https://github.com)
[![License: MIT](https://shields.io)](https://opensource.org)

A lightweight Python library powered by NumPy for building incremental and idle game mechanics.

## Installation

Install `pyncrmentl` directly from PyPI:

```bash
pip install pyncrmentl
```

## Features

* **Core Management** (`pyncrmentl.manager`): Coordinates game loops, state updates, and progression tracking.
* **Precinct & Progression Systems** (`pyncrmentl.precint`): Handles structured tiers, zones, or milestone progression.
* **Essential Mechanics** (`pyncrmentl.basic`):
  * `currency`: Fast, NumPy-backed resource and currency scaling.
  * `upgrade`: Cost curves and multiplier calculations for repeatable upgrades.
  * `reset`: Prestige and soft-reset logic with reward scaling.
  * `challenge`: Custom constraint modifiers and completion tracking.

## Quick Start

```python
import pyncrmentl
from pyncrmentl import *
import time
inc_manager = Manager(currencies=Currency("Points", persec = 0, starting = 0))
Manager.begin_game()
time.sleep(1000)
print(Manager[points]) # returns 1
```

## Project Structure

```text
pyncrmentl/
├── __init__.py
├── manager.py
├── precint.py
└── basic/
    ├── __init__.py
    ├── challenge.py
    ├── currency.py
    ├── reset.py
    └── upgrade.py
```

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/new-mechanic`).
3. Commit your changes and push to your fork.
4. Open a Pull Request.

## License

Distributed under the MIT License. See `LICENSE` for more information.