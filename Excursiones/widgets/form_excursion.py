from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QTextEdit, QPushButton, QComboBox, QMessageBox
import sqlite3
from database import DB_NAME

class FormExcursionWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Nombre de la Excursión:"))
        self.input_nombre = QLineEdit()
        layout.addWidget(self.input_nombre)

        layout.addWidget(QLabel("Duración:"))
        self.input_duracion = QLineEdit()
        layout.addWidget(self.input_duracion)

        layout.addWidget(QLabel("Descripción:"))
        self.input_descripcion = QTextEdit()
        layout.addWidget(self.input_descripcion)

        layout.addWidget(QLabel("Precio (ARS):"))
        self.input_precio = QLineEdit()
        layout.addWidget(self.input_precio)

        layout.addWidget(QLabel("Tipo de Excursión:"))
        self.combo_tipo = QComboBox()
        self.combo_tipo.addItems(["Parque", "Canal", "Lagos"])
        layout.addWidget(self.combo_tipo)

        layout.addWidget(QLabel("Detalle Extra (tren, pingüinera, etc.):"))
        self.input_extra = QLineEdit()
        layout.addWidget(self.input_extra)

        self.boton_guardar = QPushButton("Guardar Excursión")
        self.boton_guardar.clicked.connect(self.guardar_excursion)
        layout.addWidget(self.boton_guardar)

        self.setLayout(layout)

    def guardar_excursion(self):
        nombre = self.input_nombre.text()
        duracion = self.input_duracion.text()
        descripcion = self.input_descripcion.toPlainText()
        precio = self.input_precio.text()
        tipo = self.combo_tipo.currentText()
        extra = self.input_extra.text()

        if not nombre or not duracion or not descripcion or not precio:
            QMessageBox.warning(self, "Error", "Todos los campos obligatorios deben completarse.")
            return

        try:
            precio = float(precio)
        except ValueError:
            QMessageBox.warning(self, "Error", "El precio debe ser un número válido.")
            return

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO excursiones (nombre, duracion, descripcion, precio, tipo, extra)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nombre, duracion, descripcion, precio, tipo, extra))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Éxito", "Excursión guardada correctamente.")
        self.input_nombre.clear()
        self.input_duracion.clear()
        self.input_descripcion.clear()
        self.input_precio.clear()
        self.input_extra.clear()