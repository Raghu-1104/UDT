# UDS-over-CAN Modular Tool

A cross-platform, modular Python tool for emulating a UDS (Unified Diagnostic Services, ISO 14229) server and client over CAN. Supports real and virtual CAN, demo mode, logging, error injection, and flexible sensor/service extension.

## Features
- UDS server and client (ISO 14229)
- Modular service and sensor architecture
- Real CAN (SocketCAN, PCAN) and virtual CAN support
- Demo mode for users without hardware
- CLI for sending/receiving diagnostic requests
- Logging and error injection
- Example scripts and documentation

## Architecture
- **core/**: UDS protocol logic, service registry
- **transports/**: CAN hardware/virtual/demo interfaces
- **services/**: UDS service modules (e.g., ReadDTC, ECUReset)
- **sensors/**: Sensor abstraction and simulation
- **cli/**: Command-line interface
- **examples/**: Example diagnostic scripts
- **docs/**: Protocol and usage documentation 