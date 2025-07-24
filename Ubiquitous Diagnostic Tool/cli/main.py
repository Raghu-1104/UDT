import click
from rich.console import Console
from core.uds_core import UDSCore
from services.read_dtc import ReadDTCService
from services.clear_dtc import ClearDTCService
from services.read_data_by_identifier import ReadDataByIdentifierService
from services.ecu_reset import ECUResetService
from sensors.sensor_base import Sensor, SensorRegistry

console = Console()

# Global objects
uds_core = UDSCore()
sensor_registry = SensorRegistry()

# Register core UDS services
uds_core.register_service(ReadDTCService())
uds_core.register_service(ClearDTCService())
uds_core.register_service(ReadDataByIdentifierService())
uds_core.register_service(ECUResetService())

@click.group()
def cli():
    """UDS-over-CAN Modular Tool CLI"""
    pass

@cli.command()
@click.argument('service_id', type=lambda x: int(x, 16))
@click.argument('data', type=str)
def send(service_id, data):
    """Send a UDS request (hex service_id, hex data)."""
    req = bytes([service_id]) + bytes.fromhex(data)
    resp = uds_core.handle_request(req, {'sensors': sensor_registry})
    console.print(f"[bold green]Response:[/bold green] {resp.hex()}")

@cli.command()
def list_sensors():
    """List all registered sensors."""
    for sid, sensor in sensor_registry.sensors.items():
        status = "[red]MALFUNCTION[/red]" if sensor.malfunction else "[green]OK[/green]"
        console.print(f"[bold]{sid}[/bold]: {sensor.name} - {status}")

@cli.command()
@click.argument('sensor_id')
@click.argument('name')
def add_sensor(sensor_id, name):
    """Add a new simulated sensor."""
    sensor = Sensor(sensor_id, name)
    sensor_registry.add_sensor(sensor)
    console.print(f"Added sensor {name} with ID {sensor_id}")

@cli.command()
@click.argument('sensor_id')
def remove_sensor(sensor_id):
    """Remove a sensor by ID."""
    sensor_registry.remove_sensor(sensor_id)
    console.print(f"Removed sensor {sensor_id}")

@cli.command()
def detect_malfunctions():
    """Detect and list malfunctioning sensors."""
    mal = sensor_registry.detect_malfunctions()
    if not mal:
        console.print("[green]No malfunctions detected.[/green]")
    else:
        for sid, name in mal.items():
            console.print(f"[red]{sid}: {name} MALFUNCTION[/red]")

@cli.command()
@click.argument('sensor_id')
@click.argument('value')
def simulate_sensor(sensor_id, value):
    """Simulate a value for a sensor."""
    sensor = sensor_registry.get_sensor(sensor_id)
    if not sensor:
        console.print(f"[red]Sensor {sensor_id} not found.[/red]")
        return
    sensor.simulate(value)
    console.print(f"Simulated value {value} for sensor {sensor_id}")

@cli.command()
@click.argument('sensor_id')
@click.argument('state', type=bool)
def set_malfunction(sensor_id, state):
    """Set malfunction state for a sensor (True/False)."""
    sensor = sensor_registry.get_sensor(sensor_id)
    if not sensor:
        console.print(f"[red]Sensor {sensor_id} not found.[/red]")
        return
    sensor.set_malfunction(state)
    console.print(f"Set malfunction={state} for sensor {sensor_id}")

@cli.command()
def demo_mode():
    """Activate demo mode (simulated CAN and sensors)."""
    console.print("[yellow]Demo mode activated. All operations are simulated.[/yellow]")
    # In a real implementation, switch to DemoCANInterface, etc.

@cli.command()
def log():
    """Show recent log entries (stub)."""
    console.print("[blue]Logging not yet implemented.[/blue]")

if __name__ == '__main__':
    cli() 