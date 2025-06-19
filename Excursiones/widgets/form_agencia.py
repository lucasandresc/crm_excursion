from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
import sqlite3
from database import DB_NAME

class FormAgenciaWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Nombre de la Agencia:"))
        self.input_nombre = QLineEdit()
        layout.addWidget(self.input_nombre)

        layout.addWidget(QLabel("Dirección:"))
        self.input_direccion = QLineEdit()
        layout.addWidget(self.input_direccion)

        layout.addWidget(QLabel("Teléfono:"))
        self.input_telefono = QLineEdit()
        layout.addWidget(self.input_telefono)

        layout.addWidget(QLabel("Email:"))
        self.input_email = QLineEdit()
        layout.addWidget(self.input_email)

        self.boton_guardar = QPushButton("Guardar Agencia")
        self.boton_guardar.clicked.connect(self.guardar_agencia)
        layout.addWidget(self.boton_guardar)

        self.setLayout(layout)

    def guardar_agencia(self):
        nombre = self.input_nombre.text()
        direccion = self.input_direccion.text()
        telefono = self.input_telefono.text()
        email = self.input_email.text()

        if not nombre:
            QMessageBox.warning(self, "Error", "El nombre es obligatorio.")
            return

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO agencias (nombre, direccion, telefono, email)
            VALUES (?, ?, ?, ?)
        """, (nombre, direccion, telefono, email))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Éxito", "Agencia guardada correctamente.")
        self.input_nombre.clear()
        self.input_direccion.clear()
        self.input_telefono.clear()
        self.input_email.clear()
