from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QListWidget, QMessageBox
)
from sensors.sensor_base import Sensor, SensorRegistry

class SensorsPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.sensor_registry = SensorRegistry()
        self.init_ui()
        self.refresh_sensor_list()

    def init_ui(self):
        layout = QVBoxLayout()

        # Sensor list
        layout.addWidget(QLabel("Sensors:"))
        self.sensor_list = QListWidget()
        layout.addWidget(self.sensor_list)

        # Add sensor
        add_layout = QHBoxLayout()
        self.add_id_input = QLineEdit()
        self.add_id_input.setPlaceholderText("Sensor ID")
        self.add_name_input = QLineEdit()
        self.add_name_input.setPlaceholderText("Sensor Name")
        self.add_btn = QPushButton("Add Sensor")
        add_layout.addWidget(self.add_id_input)
        add_layout.addWidget(self.add_name_input)
        add_layout.addWidget(self.add_btn)
        layout.addLayout(add_layout)

        # Remove sensor
        self.remove_btn = QPushButton("Remove Selected Sensor")
        layout.addWidget(self.remove_btn)

        # Simulate value
        sim_layout = QHBoxLayout()
        self.sim_id_input = QLineEdit()
        self.sim_id_input.setPlaceholderText("Sensor ID")
        self.sim_value_input = QLineEdit()
        self.sim_value_input.setPlaceholderText("Value")
        self.sim_btn = QPushButton("Simulate Value")
        sim_layout.addWidget(self.sim_id_input)
        sim_layout.addWidget(self.sim_value_input)
        sim_layout.addWidget(self.sim_btn)
        layout.addLayout(sim_layout)

        # Set malfunction
        mal_layout = QHBoxLayout()
        self.mal_id_input = QLineEdit()
        self.mal_id_input.setPlaceholderText("Sensor ID")
        self.mal_btn = QPushButton("Toggle Malfunction")
        mal_layout.addWidget(self.mal_id_input)
        mal_layout.addWidget(self.mal_btn)
        layout.addLayout(mal_layout)

        self.setLayout(layout)

        # Connect signals
        self.add_btn.clicked.connect(self.add_sensor)
        self.remove_btn.clicked.connect(self.remove_sensor)
        self.sim_btn.clicked.connect(self.simulate_value)
        self.mal_btn.clicked.connect(self.toggle_malfunction)

    def refresh_sensor_list(self):
        self.sensor_list.clear()
        for sid, sensor in self.sensor_registry.sensors.items():
            status = "[MALFUNCTION]" if sensor.malfunction else "[OK]"
            self.sensor_list.addItem(f"{sid}: {sensor.name} {status}")

    def add_sensor(self):
        sid = self.add_id_input.text()
        name = self.add_name_input.text()
        if not sid or not name:
            QMessageBox.warning(self, "Input Error", "Please enter both Sensor ID and Name.")
            return
        if self.sensor_registry.get_sensor(sid):
            QMessageBox.warning(self, "Duplicate", f"Sensor {sid} already exists.")
            return
        sensor = Sensor(sid, name)
        self.sensor_registry.add_sensor(sensor)
        self.refresh_sensor_list()
        self.add_id_input.clear()
        self.add_name_input.clear()

    def remove_sensor(self):
        row = self.sensor_list.currentRow()
        if row >= 0:
            item = self.sensor_list.item(row)
            sid = item.text().split(':')[0]
            self.sensor_registry.remove_sensor(sid)
            self.refresh_sensor_list()

    def simulate_value(self):
        sid = self.sim_id_input.text()
        value = self.sim_value_input.text()
        sensor = self.sensor_registry.get_sensor(sid)
        if not sensor:
            QMessageBox.warning(self, "Not Found", f"Sensor {sid} not found.")
            return
        sensor.simulate(value)
        QMessageBox.information(self, "Simulate Value", f"Simulated value {value} for sensor {sid}")
        self.sim_id_input.clear()
        self.sim_value_input.clear()

    def toggle_malfunction(self):
        sid = self.mal_id_input.text()
        sensor = self.sensor_registry.get_sensor(sid)
        if not sensor:
            QMessageBox.warning(self, "Not Found", f"Sensor {sid} not found.")
            return
        sensor.set_malfunction(not sensor.malfunction)
        self.refresh_sensor_list()
        QMessageBox.information(self, "Toggle Malfunction", f"Toggled malfunction for sensor {sid}")
        self.mal_id_input.clear() 