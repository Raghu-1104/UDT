import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QTabWidget, QVBoxLayout, QLabel, QStatusBar, QPushButton
)
from PyQt5.QtGui import QIcon, QFont
import qdarkstyle
from gui.uds_panel import UDSPanel
from gui.sensors_panel import SensorsPanel
from gui.logs_panel import LogsPanel
from gui.settings_panel import SettingsPanel
from gui.protocol_editor_panel import ProtocolEditorPanel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.font_size = 16  # Default font size
        self.setWindowTitle("UDS-over-CAN Diagnostic Suite (Dark Theme)")
        self.setWindowIcon(QIcon("resources/uds_icon.png"))  # Add your icon to resources/
        self.resize(1800, 1100)
        self.setMinimumSize(1500, 900)
        self.init_ui()
        self.statusBar().showMessage("Ready. Demo mode active.")

    def init_ui(self):
        # Set a much larger default font for accessibility
        font = QFont()
        font.setPointSize(self.font_size)
        self.setFont(font)

        tabs = QTabWidget()
        tabs.addTab(UDSPanel(), "UDS Requests")
        tabs.addTab(SensorsPanel(), "Sensors")
        tabs.addTab(LogsPanel(), "Logs")
        tabs.addTab(SettingsPanel(), "Settings")
        tabs.addTab(ProtocolEditorPanel(), "Protocol Editor")
        self.setCentralWidget(tabs)
        self.setStatusBar(QStatusBar())

        # Add font size controls to the status bar
        self.add_font_size_controls()

    def add_font_size_controls(self):
        status_bar = self.statusBar()
        font_label = QLabel(f"Font: {self.font_size}")
        btn_increase = QPushButton("+")
        btn_decrease = QPushButton("−")
        btn_increase.setFixedWidth(30)
        btn_decrease.setFixedWidth(30)
        status_bar.addPermanentWidget(btn_decrease)
        status_bar.addPermanentWidget(font_label)
        status_bar.addPermanentWidget(btn_increase)
        btn_increase.clicked.connect(lambda: self.change_font_size(1, font_label))
        btn_decrease.clicked.connect(lambda: self.change_font_size(-1, font_label))

    def change_font_size(self, delta, font_label):
        new_size = self.font_size + delta
        if new_size < 8:
            new_size = 8
        elif new_size > 48:
            new_size = 48
        self.font_size = new_size
        font = QFont()
        font.setPointSize(self.font_size)
        self.setFont(font)
        font_label.setText(f"Font: {self.font_size}")
        self.apply_font_recursively(self, font)

    def apply_font_recursively(self, widget, font):
        widget.setFont(font)
        for child in widget.findChildren(QWidget):
            child.setFont(font)


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 