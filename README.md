 Ubiquitous Diagnostic Tool (UDS-over-CAN Modular Tool)

A cross-platform, modular Python tool for emulating a UDS (Unified Diagnostic Services, ISO 14229) server and client over CAN. Supports real and virtual CAN, demo mode, logging, error injection, and flexible sensor/service extension.

---

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
  - [Command-Line Interface (CLI)](#command-line-interface-cli)
  - [Graphical User Interface (GUI)](#graphical-user-interface-gui)
  - [Examples](#examples)
- [Supported UDS Services](#supported-uds-services)
- [Extending the Tool](#extending-the-tool)
- [Development](#development)
- [License](#license)

---

## Features

- UDS server and client (ISO 14229)
- Modular service and sensor architecture
- Real CAN (SocketCAN, PCAN) and virtual CAN support
- Demo mode for users without hardware
- CLI for sending/receiving diagnostic requests
- PyQt5-based GUI for interactive diagnostics
- Logging and error injection
- Example scripts and documentation

---

## Architecture

- **core/**: UDS protocol logic, service registry, logging, error injection
- **transports/**: CAN hardware/virtual/demo interfaces
- **services/**: UDS service modules (e.g., ReadDTC, ECUReset, ClearDTC, ReadDataByIdentifier)
- **sensors/**: Sensor abstraction and simulation
- **cli/**: Command-line interface
- **gui/**: PyQt5 GUI components (main window, protocol editor, logs, sensors, UDS panel, settings)
- **examples/**: Example diagnostic scripts
- **docs/**: Protocol and usage documentation

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ubiquitous-diagnostic-tool.git
   cd ubiquitous-diagnostic-tool
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   **Dependencies:**
   - python-can
   - click
   - rich
   - PyQt5
   - qdarkstyle
   - cantools
   - pyuavcan

---

## Usage

### Command-Line Interface (CLI)

The CLI allows you to send and receive UDS diagnostic requests, inject errors, and log activity.

```bash
python -m cli.main --help
```

### Graphical User Interface (GUI)

The GUI provides an interactive environment for diagnostics, protocol editing, sensor monitoring, and more.

```bash
python gui/main_window.py
```

### Examples

Example scripts are available in the `examples/` directory:

- `read_dtc_example.py`
- `clear_dtc_example.py`
- `ecu_reset_example.py`
- `read_data_by_identifier_example.py`

Run an example:
```bash
python examples/read_dtc_example.py
```

---

## Supported UDS Services

- **ReadDTC** (`read_dtc.py`)
- **ClearDTC** (`clear_dtc.py`)
- **ECUReset** (`ecu_reset.py`)
- **ReadDataByIdentifier** (`read_data_by_identifier.py`)

---

## Extending the Tool

- **Add new UDS services:** Implement a new module in `services/` and register it in the core.
- **Add new sensors:** Extend the base class in `sensors/`.
- **Add new CAN interfaces:** Implement in `transports/`.

See the `docs/` directory for protocol logic and usage documentation.

---

## Development

- Code style: PEP8
- Logging: See `core/logging.py`
- Error injection: See `core/error_injection.py`
- GUI: PyQt5, see `gui/` modules

---

## License

[MIT License](LICENSE) (or specify your license here)

---

## Contributing

Pull requests and issues are welcome! Please see the `docs/` directory for more information on contributing and extending the tool.
