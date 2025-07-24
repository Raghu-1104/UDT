# UDS-over-CAN Tool Usage

## Running the CLI

```
python -m cli.main [COMMAND] [ARGS...]
```

## Common Commands

- `send SERVICE_ID DATA` — Send a UDS request (hex values)
- `list_sensors` — List all registered sensors
- `add_sensor SENSOR_ID NAME` — Add a new simulated sensor
- `remove_sensor SENSOR_ID` — Remove a sensor
- `simulate_sensor SENSOR_ID VALUE` — Simulate a value for a sensor
- `set_malfunction SENSOR_ID STATE` — Set malfunction state (True/False)
- `detect_malfunctions` — List malfunctioning sensors
- `demo_mode` — Activate demo mode (no hardware required)
- `log` — Show recent log entries

## Demo Mode

Run `python -m cli.main demo_mode` to activate full simulation (no CAN hardware needed).

## Example Scripts

Run example scripts from the `examples/` directory:

```
python examples/read_dtc_example.py
python examples/clear_dtc_example.py
python examples/read_data_by_identifier_example.py
python examples/ecu_reset_example.py
```

## Extending the Tool

- Add new UDS services: create a new module in `services/` inheriting from `UDSService` and register it in the CLI or main app.
- Add new sensors: subclass `Sensor` and register with the `SensorRegistry`.

See `context.md` for architecture details. 