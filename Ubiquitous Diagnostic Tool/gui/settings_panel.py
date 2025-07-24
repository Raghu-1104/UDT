from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QCheckBox, QPushButton, QMessageBox
)
from core.error_injection import ErrorInjector

class SettingsPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.error_injector = ErrorInjector()
        self.selected_can = "DemoCAN"
        self.demo_mode = True
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # CAN interface selection
        can_layout = QHBoxLayout()
        can_layout.addWidget(QLabel("CAN Interface:"))
        self.can_combo = QComboBox()
        self.can_combo.addItems(["SocketCAN", "PCAN", "VirtualCAN", "DemoCAN"])
        self.can_combo.setCurrentText(self.selected_can)
        can_layout.addWidget(self.can_combo)
        layout.addLayout(can_layout)

        # Demo mode toggle
        self.demo_checkbox = QCheckBox("Enable Demo Mode (no hardware)")
        self.demo_checkbox.setChecked(self.demo_mode)
        layout.addWidget(self.demo_checkbox)

        # Error injection controls
        layout.addWidget(QLabel("Error Injection:"))
        self.can_error_checkbox = QCheckBox("Inject CAN Error")
        self.uds_error_checkbox = QCheckBox("Inject UDS Error")
        layout.addWidget(self.can_error_checkbox)
        layout.addWidget(self.uds_error_checkbox)

        # Apply button
        self.apply_btn = QPushButton("Apply Settings")
        layout.addWidget(self.apply_btn)

        self.setLayout(layout)

        self.apply_btn.clicked.connect(self.apply_settings)

    def apply_settings(self):
        self.selected_can = self.can_combo.currentText()
        self.demo_mode = self.demo_checkbox.isChecked()
        self.error_injector.enable_can_error(self.can_error_checkbox.isChecked())
        self.error_injector.enable_uds_error(self.uds_error_checkbox.isChecked())
        QMessageBox.information(self, "Settings Applied", f"CAN: {self.selected_can}\nDemo Mode: {self.demo_mode}\nCAN Error: {self.can_error_checkbox.isChecked()}\nUDS Error: {self.uds_error_checkbox.isChecked()}") 