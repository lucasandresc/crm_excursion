from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem
import sqlite3
from database import DB_NAME

class ListadoReservasWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())

        self.layout().addWidget(QLabel("Listado de Reservas Registradas"))
        self.tabla = QTableWidget()
        self.layout().addWidget(self.tabla)

        self.cargar_reservas()

    def cargar_reservas(self):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT r.fecha, a.nombre, e.nombre
            FROM reservas r
            JOIN agencias a ON r.agencia_id = a.id
            JOIN excursiones e ON r.excursion_id = e.id
            ORDER BY r.fecha DESC
        """)
        reservas = cursor.fetchall()
        conn.close()

        self.tabla.setColumnCount(3)
        self.tabla.setHorizontalHeaderLabels(["Fecha", "Agencia", "Excursión"])
        self.tabla.setRowCount(len(reservas))

        for fila_idx, (fecha, agencia, excursion) in enumerate(reservas):
            self.tabla.setItem(fila_idx, 0, QTableWidgetItem(fecha))
            self.tabla.setItem(fila_idx, 1, QTableWidgetItem(agencia))
            self.tabla.setItem(fila_idx, 2, QTableWidgetItem(excursion))