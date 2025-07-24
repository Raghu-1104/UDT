from typing import Any, Dict, Callable

class Sensor:
    """
    Base class for all sensors. Subclass this to implement specific sensor types.
    """
    def __init__(self, sensor_id: str, name: str, malfunction: bool = False):
        self.sensor_id = sensor_id
        self.name = name
        self.malfunction = malfunction
        self.value = None

    def read(self) -> Any:
        """Read the current sensor value. Override in subclasses."""
        if self.malfunction:
            raise Exception(f"Sensor {self.name} malfunction detected!")
        return self.value

    def simulate(self, value: Any):
        """Simulate a sensor value (for demo/testing)."""
        self.value = value

    def set_malfunction(self, state: bool):
        self.malfunction = state


class SensorRegistry:
    """
    Registry for managing sensors. Allows adding, removing, and looking up sensors.
    """
    def __init__(self):
        self.sensors: Dict[str, Sensor] = {}

    def add_sensor(self, sensor: Sensor):
        self.sensors[sensor.sensor_id] = sensor

    def remove_sensor(self, sensor_id: str):
        if sensor_id in self.sensors:
            del self.sensors[sensor_id]

    def get_sensor(self, sensor_id: str) -> Sensor:
        return self.sensors.get(sensor_id)

    def detect_malfunctions(self) -> Dict[str, str]:
        """Return a dict of sensor_id: name for all malfunctioning sensors."""
        return {sid: s.name for sid, s in self.sensors.items() if s.malfunction}

    def simulate_all(self, value_func: Callable[[Sensor], Any]):
        """Simulate all sensors using a value function."""
        for sensor in self.sensors.values():
            sensor.simulate(value_func(sensor)) 