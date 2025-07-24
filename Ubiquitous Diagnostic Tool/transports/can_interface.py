from abc import ABC, abstractmethod
from typing import Callable, Optional

class CANInterface(ABC):
    """
    Abstract base class for CAN transport. All CAN backends should inherit from this.
    """
    def __init__(self, channel: str, bitrate: int = 500000, rx_callback: Optional[Callable] = None):
        self.channel = channel
        self.bitrate = bitrate
        self.rx_callback = rx_callback

    @abstractmethod
    def start(self):
        """Start the CAN interface."""
        pass

    @abstractmethod
    def stop(self):
        """Stop the CAN interface."""
        pass

    @abstractmethod
    def send(self, can_id: int, data: bytes):
        """Send a CAN frame."""
        pass

    @abstractmethod
    def set_rx_callback(self, callback: Callable):
        """Set a callback for received CAN frames."""
        pass


class SocketCANInterface(CANInterface):
    def start(self):
        # TODO: Implement SocketCAN startup logic
        pass
    def stop(self):
        # TODO: Implement SocketCAN stop logic
        pass
    def send(self, can_id: int, data: bytes):
        # TODO: Implement SocketCAN send logic
        pass
    def set_rx_callback(self, callback: Callable):
        self.rx_callback = callback


class PCANInterface(CANInterface):
    def start(self):
        # TODO: Implement PCAN startup logic
        pass
    def stop(self):
        # TODO: Implement PCAN stop logic
        pass
    def send(self, can_id: int, data: bytes):
        # TODO: Implement PCAN send logic
        pass
    def set_rx_callback(self, callback: Callable):
        self.rx_callback = callback


class VirtualCANInterface(CANInterface):
    def start(self):
        # TODO: Implement virtual CAN startup logic
        pass
    def stop(self):
        # TODO: Implement virtual CAN stop logic
        pass
    def send(self, can_id: int, data: bytes):
        # TODO: Implement virtual CAN send logic
        pass
    def set_rx_callback(self, callback: Callable):
        self.rx_callback = callback


class DemoCANInterface(CANInterface):
    def start(self):
        # TODO: Implement demo CAN startup logic (simulate CAN bus)
        pass
    def stop(self):
        # TODO: Implement demo CAN stop logic
        pass
    def send(self, can_id: int, data: bytes):
        # TODO: Implement demo CAN send logic (simulate response)
        pass
    def set_rx_callback(self, callback: Callable):
        self.rx_callback = callback 