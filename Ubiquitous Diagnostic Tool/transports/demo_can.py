from transports.can_interface import CANInterface
from core.logging import UDSLogger
from core.error_injection import ErrorInjector

class DemoCANInterface(CANInterface):
    def __init__(self, channel='demo', bitrate=500000, rx_callback=None):
        super().__init__(channel, bitrate, rx_callback)
        self.logger = UDSLogger()
        self.error_injector = ErrorInjector()
        self.running = False

    def start(self):
        self.running = True
        self.logger.log('DemoCANInterface started (simulated CAN bus)')

    def stop(self):
        self.running = False
        self.logger.log('DemoCANInterface stopped')

    def send(self, can_id: int, data: bytes):
        if self.error_injector.should_inject_can_error():
            self.logger.log(f'Injected CAN error on send: id={can_id:03X}, data={data.hex()}', level=40)
            return  # Simulate dropped frame
        self.logger.log(f'Sent CAN frame (simulated): id={can_id:03X}, data={data.hex()}')
        # Simulate immediate loopback for demo
        if self.rx_callback:
            self.rx_callback(can_id, data)

    def set_rx_callback(self, callback):
        self.rx_callback = callback
        self.logger.log('DemoCANInterface RX callback set') 