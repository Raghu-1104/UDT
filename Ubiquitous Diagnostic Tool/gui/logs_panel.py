from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
from core.logging import UDSLogger

class LogsPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.logger = UDSLogger()
        self.init_ui()
        self.refresh_logs()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Recent Logs:"))
        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        layout.addWidget(self.log_box)
        self.refresh_btn = QPushButton("Refresh Logs")
        layout.addWidget(self.refresh_btn)
        self.setLayout(layout)
        self.refresh_btn.clicked.connect(self.refresh_logs)

    def refresh_logs(self):
        self.log_box.clear()
        for level, msg in self.logger.get_recent(50):
            self.log_box.append(f"[{level}] {msg}") 