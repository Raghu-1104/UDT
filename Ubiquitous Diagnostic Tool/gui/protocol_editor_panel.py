from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem,
    QFormLayout, QLineEdit, QComboBox, QFileDialog, QMessageBox, QGroupBox
)
import os
import cantools
from PyQt5.QtCore import Qt

class ProtocolEditorPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Title
        title = QLabel("Protocol Editor (DroneCAN/DBC)")
        title.setStyleSheet("font-size: 18pt; font-weight: bold;")
        main_layout.addWidget(title)

        # Message List Section
        msg_group = QGroupBox("Messages")
        msg_layout = QVBoxLayout()
        self.msg_table = QTableWidget(0, 2)
        self.msg_table.setHorizontalHeaderLabels(["Name", "ID"])
        self.msg_table.setEditTriggers(QTableWidget.DoubleClicked | QTableWidget.SelectedClicked)
        msg_layout.addWidget(self.msg_table)
        btn_layout = QHBoxLayout()
        self.add_msg_btn = QPushButton("Add Message")
        self.remove_msg_btn = QPushButton("Remove Message")
        btn_layout.addWidget(self.add_msg_btn)
        btn_layout.addWidget(self.remove_msg_btn)
        msg_layout.addLayout(btn_layout)
        msg_group.setLayout(msg_layout)
        main_layout.addWidget(msg_group)

        # Message Details Section
        details_group = QGroupBox("Message Details")
        details_layout = QFormLayout()
        self.msg_name_edit = QLineEdit()
        self.msg_id_edit = QLineEdit()
        details_layout.addRow("Name:", self.msg_name_edit)
        details_layout.addRow("ID:", self.msg_id_edit)
        details_group.setLayout(details_layout)
        main_layout.addWidget(details_group)

        # Fields Section
        fields_group = QGroupBox("Fields")
        fields_layout = QVBoxLayout()
        self.fields_table = QTableWidget(0, 3)
        self.fields_table.setHorizontalHeaderLabels(["Name", "Type", "Length (bits)"])
        self.fields_table.setEditTriggers(QTableWidget.DoubleClicked | QTableWidget.SelectedClicked)
        fields_layout.addWidget(self.fields_table)
        field_btn_layout = QHBoxLayout()
        self.add_field_btn = QPushButton("Add Field")
        self.remove_field_btn = QPushButton("Remove Field")
        field_btn_layout.addWidget(self.add_field_btn)
        field_btn_layout.addWidget(self.remove_field_btn)
        fields_layout.addLayout(field_btn_layout)
        fields_group.setLayout(fields_layout)
        main_layout.addWidget(fields_group)

        # Import/Export Buttons
        io_layout = QHBoxLayout()
        self.import_btn = QPushButton("Import Protocol (DSDL/DBC)")
        self.export_btn = QPushButton("Export Protocol (DSDL/DBC)")
        io_layout.addWidget(self.import_btn)
        io_layout.addWidget(self.export_btn)
        main_layout.addLayout(io_layout)

        # Connect buttons to methods
        self.import_btn.clicked.connect(self.import_protocol)
        self.export_btn.clicked.connect(self.export_protocol)
        self.add_msg_btn.clicked.connect(self.add_message)
        self.remove_msg_btn.clicked.connect(self.remove_message)
        self.add_field_btn.clicked.connect(self.add_field)
        self.remove_field_btn.clicked.connect(self.remove_field)
        self.msg_table.cellChanged.connect(self.update_message_from_table)
        self.fields_table.cellChanged.connect(self.update_field_from_table)

        # Set main layout
        self.setLayout(main_layout)

    def import_protocol(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Import Protocol", "", "Protocol Files (*.uavcan *.dsdl *.dbc);;All Files (*)")
        if file_path:
            ext = os.path.splitext(file_path)[1].lower()
            try:
                if ext == ".dbc":
                    self.load_dbc(file_path)
                elif ext in (".uavcan", ".dsdl"):
                    QMessageBox.information(self, "Import", "DSDL import not yet implemented.")
                    return
                else:
                    QMessageBox.warning(self, "Import", "Unsupported file type.")
                    return
                QMessageBox.information(self, "Import", f"Imported protocol from:\n{file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Import Error", f"Failed to import protocol:\n{str(e)}")

    def load_dbc(self, file_path):
        db = cantools.database.load_file(file_path)
        self.messages = []
        self.msg_table.setRowCount(0)
        self.fields_table.setRowCount(0)
        for msg in db.messages:
            msg_dict = {
                'name': msg.name,
                'id': msg.frame_id,
                'fields': []
            }
            row = self.msg_table.rowCount()
            self.msg_table.insertRow(row)
            self.msg_table.setItem(row, 0, QTableWidgetItem(msg.name))
            self.msg_table.setItem(row, 1, QTableWidgetItem(hex(msg.frame_id)))
            for sig in msg.signals:
                field = {
                    'name': sig.name,
                    'type': 'float' if sig.is_float else ('signed' if sig.is_signed else 'unsigned'),
                    'length': sig.length
                }
                msg_dict['fields'].append(field)
            self.messages.append(msg_dict)
        # Optionally, select the first message and show its fields
        if self.messages:
            self.show_message_fields(0)
        self.msg_table.selectRow(0)
        self.msg_table.cellClicked.connect(self.show_message_fields)

    def show_message_fields(self, row, col=None):
        if not hasattr(self, 'messages') or row >= len(self.messages):
            self.fields_table.setRowCount(0)
            return
        fields = self.messages[row]['fields']
        self.fields_table.setRowCount(0)
        for i, field in enumerate(fields):
            self.fields_table.insertRow(i)
            self.fields_table.setItem(i, 0, QTableWidgetItem(field['name']))
            self.fields_table.setItem(i, 1, QTableWidgetItem(field['type']))
            self.fields_table.setItem(i, 2, QTableWidgetItem(str(field['length'])))

    def export_protocol(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Export Protocol", "", "Protocol Files (*.uavcan *.dsdl *.dbc);;All Files (*)")
        if file_path:
            ext = os.path.splitext(file_path)[1].lower()
            try:
                if ext == ".dbc":
                    self.save_dbc(file_path)
                elif ext in (".uavcan", ".dsdl"):
                    QMessageBox.information(self, "Export", "DSDL export not yet implemented.")
                    return
                else:
                    QMessageBox.warning(self, "Export", "Unsupported file type.")
                    return
                QMessageBox.information(self, "Export", f"Exported protocol to:\n{file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Export Error", f"Failed to export protocol:\n{str(e)}")

    def add_message(self):
        if not hasattr(self, 'messages'):
            self.messages = []
        msg_name = f"Message{len(self.messages)+1}"
        msg_id = self.get_next_free_id()
        msg_dict = {'name': msg_name, 'id': msg_id, 'fields': []}
        self.messages.append(msg_dict)
        row = self.msg_table.rowCount()
        self.msg_table.insertRow(row)
        self.msg_table.setItem(row, 0, QTableWidgetItem(msg_name))
        self.msg_table.setItem(row, 1, QTableWidgetItem(str(msg_id)))
        self.msg_table.selectRow(row)
        self.show_message_fields(row)

    def remove_message(self):
        row = self.msg_table.currentRow()
        if row >= 0 and hasattr(self, 'messages') and row < len(self.messages):
            self.msg_table.removeRow(row)
            del self.messages[row]
            if self.messages:
                self.show_message_fields(0)
                self.msg_table.selectRow(0)
            else:
                self.fields_table.setRowCount(0)

    def add_field(self):
        msg_row = self.msg_table.currentRow()
        if msg_row < 0 or not hasattr(self, 'messages') or msg_row >= len(self.messages):
            QMessageBox.warning(self, "Add Field", "Select a message first.")
            return
        field_name = f"field{len(self.messages[msg_row]['fields'])+1}"
        field_type = 'unsigned'
        field_length = 8
        field = {'name': field_name, 'type': field_type, 'length': field_length}
        self.messages[msg_row]['fields'].append(field)
        row = self.fields_table.rowCount()
        self.fields_table.insertRow(row)
        self.fields_table.setItem(row, 0, QTableWidgetItem(field_name))
        self.fields_table.setItem(row, 1, QTableWidgetItem(field_type))
        self.fields_table.setItem(row, 2, QTableWidgetItem(str(field_length)))

    def remove_field(self):
        msg_row = self.msg_table.currentRow()
        field_row = self.fields_table.currentRow()
        if msg_row < 0 or field_row < 0 or not hasattr(self, 'messages') or msg_row >= len(self.messages):
            return
        if field_row < len(self.messages[msg_row]['fields']):
            self.fields_table.removeRow(field_row)
            del self.messages[msg_row]['fields'][field_row]

    def update_message_from_table(self, row, col):
        if not hasattr(self, 'messages') or row >= len(self.messages):
            return
        name_item = self.msg_table.item(row, 0)
        id_item = self.msg_table.item(row, 1)
        name = name_item.text() if name_item else ''
        try:
            msg_id = int(id_item.text()) if id_item else 0
        except ValueError:
            QMessageBox.warning(self, "Invalid ID", "Message ID must be an integer.")
            return
        # Validate unique ID
        for i, msg in enumerate(self.messages):
            if i != row and msg['id'] == msg_id:
                QMessageBox.warning(self, "Duplicate ID", "Message ID must be unique.")
                return
        self.messages[row]['name'] = name
        self.messages[row]['id'] = msg_id

    def update_field_from_table(self, row, col):
        msg_row = self.msg_table.currentRow()
        if not hasattr(self, 'messages') or msg_row < 0 or msg_row >= len(self.messages):
            return
        field = self.messages[msg_row]['fields'][row]
        name_item = self.fields_table.item(row, 0)
        type_item = self.fields_table.item(row, 1)
        length_item = self.fields_table.item(row, 2)
        name = name_item.text() if name_item else ''
        ftype = type_item.text() if type_item else 'unsigned'
        try:
            flen = int(length_item.text()) if length_item else 8
        except ValueError:
            QMessageBox.warning(self, "Invalid Length", "Field length must be an integer.")
            return
        if ftype not in ['unsigned', 'signed', 'float']:
            QMessageBox.warning(self, "Invalid Type", "Field type must be unsigned, signed, or float.")
            return
        field['name'] = name
        field['type'] = ftype
        field['length'] = flen

    def get_next_free_id(self):
        used_ids = {msg['id'] for msg in getattr(self, 'messages', [])}
        for i in range(0x100):
            if i not in used_ids:
                return i
        return 0x100

    def save_dbc(self, file_path):
        import cantools
        from cantools.database.can.signal import Signal
        from cantools.database.can.message import Message
        from cantools.database.can.database import Database
        db = Database()
        for msg in getattr(self, 'messages', []):
            signals = []
            start_bit = 0
            for field in msg['fields']:
                signals.append(Signal(
                    name=field['name'],
                    start=start_bit,
                    length=int(field['length']),
                    byte_order='little_endian',
                    is_signed=(field['type'] == 'signed'),
                    is_float=(field['type'] == 'float'),
                    scale=1,
                    offset=0,
                    minimum=None,
                    maximum=None,
                    unit=None
                ))
                start_bit += int(field['length'])
            db.messages.append(Message(
                frame_id=int(msg['id']),
                name=msg['name'],
                length=8,  # Default CAN frame length
                signals=signals
            ))
        with open(file_path, 'w') as f:
            f.write(db.as_dbc_string())

    # Placeholder for DSDL import (DroneCAN)
    def load_dsdl(self, file_path):
        # TODO: Use pyuavcan.dsdl to parse and load DSDL types
        QMessageBox.information(self, "Import", "DSDL import is not yet implemented.")

    # Placeholder for DSDL export (DroneCAN)
    def save_dsdl(self, file_path):
        # TODO: Use pyuavcan.dsdl to generate and save DSDL types
        QMessageBox.information(self, "Export", "DSDL export is not yet implemented.") 