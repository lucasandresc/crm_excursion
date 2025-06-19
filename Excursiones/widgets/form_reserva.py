from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QMessageBox, QDateEdit
from PyQt5.QtCore import QDate
import sqlite3
from database import DB_NAME

class FormReservaWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())

        self.layout().addWidget(QLabel("Agencia:"))
        self.combo_agencia = QComboBox()
        self.layout().addWidget(self.combo_agencia)

        self.layout().addWidget(QLabel("Excursión:"))
        self.combo_excursion = QComboBox()
        self.layout().addWidget(self.combo_excursion)

        self.layout().addWidget(QLabel("Fecha:"))
        self.fecha_reserva = QDateEdit()
        self.fecha_reserva.setDate(QDate.currentDate())
        self.fecha_reserva.setCalendarPopup(True)
        self.layout().addWidget(self.fecha_reserva)

        self.boton_guardar = QPushButton("Registrar Reserva")
        self.boton_guardar.clicked.connect(self.guardar_reserva)
        self.layout().addWidget(self.boton_guardar)

    def actualizar(self):
        self.cargar_datos()

    def cargar_datos(self):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("SELECT id, nombre FROM agencias")
        self.agencias = cursor.fetchall()
        self.combo_agencia.clear()
        for id_agencia, nombre in self.agencias:
            self.combo_agencia.addItem(nombre, id_agencia)

        cursor.execute("SELECT id, nombre FROM excursiones")
        self.excursiones = cursor.fetchall()
        self.combo_excursion.clear()
        for id_exc, nombre in self.excursiones:
            self.combo_excursion.addItem(nombre, id_exc)

        conn.close()

    def guardar_reserva(self):
        id_agencia = self.combo_agencia.currentData()
        id_excursion = self.combo_excursion.currentData()
        fecha = self.fecha_reserva.date().toString("yyyy-MM-dd")

        if not id_agencia or not id_excursion:
            QMessageBox.warning(self, "Error", "Debes seleccionar una agencia y una excursión.")
            return

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO reservas (agencia_id, excursion_id, fecha)
            VALUES (?, ?, ?)
        """, (id_agencia, id_excursion, fecha))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Éxito", "Reserva registrada correctamente.")
        self.actualizar()