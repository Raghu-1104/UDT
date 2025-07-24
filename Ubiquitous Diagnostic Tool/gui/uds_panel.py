from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QLineEdit, QTextEdit
)
from core.uds_core import UDSCore
from services.read_dtc import ReadDTCService
from services.clear_dtc import ClearDTCService
from services.read_data_by_identifier import ReadDataByIdentifierService
from services.ecu_reset import ECUResetService
from sensors.sensor_base import SensorRegistry
from core.logging import UDSLogger

class UDSPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.uds_core = UDSCore()
        self.sensor_registry = SensorRegistry()
        self.logger = UDSLogger()
        self._register_services()
        self.init_ui()

    def _register_services(self):
        self.uds_core.register_service(ReadDTCService())
        self.uds_core.register_service(ClearDTCService())
        self.uds_core.register_service(ReadDataByIdentifierService())
        self.uds_core.register_service(ECUResetService())

    def init_ui(self):
        layout = QVBoxLayout()

        # Service selection
        service_layout = QHBoxLayout()
        service_layout.addWidget(QLabel("Service:"))
        self.service_combo = QComboBox()
        self.service_combo.addItems([
            "ReadDTC (0x19)",
            "ClearDTC (0x14)",
            "ReadDataByIdentifier (0x22)",
            "ECUReset (0x11)"
        ])
        service_layout.addWidget(self.service_combo)
        layout.addLayout(service_layout)

        # Data input
        data_layout = QHBoxLayout()
        data_layout.addWidget(QLabel("Data (hex):"))
        self.data_input = QLineEdit()
        data_layout.addWidget(self.data_input)
        layout.addLayout(data_layout)

        # Send button
        self.send_btn = QPushButton("Send Request")
        layout.addWidget(self.send_btn)

        # Response display
        layout.addWidget(QLabel("Response:"))
        self.response_box = QTextEdit()
        self.response_box.setReadOnly(True)
        layout.addWidget(self.response_box)

        self.setLayout(layout)

        # Connect signals
        self.send_btn.clicked.connect(self.send_request)

    def send_request(self):
        service_map = {
            0: 0x19,  # ReadDTC
            1: 0x14,  # ClearDTC
            2: 0x22,  # ReadDataByIdentifier
            3: 0x11,  # ECUReset
        }
        idx = self.service_combo.currentIndex()
        service_id = service_map.get(idx)
        data_hex = self.data_input.text().replace(' ', '')
        try:
            data_bytes = bytes.fromhex(data_hex) if data_hex else b''
        except ValueError:
            self.response_box.append("[Error] Invalid hex data.")
            return
        req = bytes([service_id]) + data_bytes
        self.logger.log(f"[GUI] Sent UDS request: {req.hex()}")
        resp = self.uds_core.handle_request(req, {'sensors': self.sensor_registry})
        self.logger.log(f"[GUI] Received UDS response: {resp.hex()}")
        self.response_box.append(f"[Sent] {service_id:02X} | Data: {data_hex}")
        self.response_box.append(f"[Response] {resp.hex()}\n") 