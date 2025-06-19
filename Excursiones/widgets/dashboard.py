from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QFrame
from PyQt5.QtGui import QFont
from database import contar_excursiones, contar_agencias, contar_reservas

class DashboardWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout_general = QVBoxLayout()

        self.titulo = QLabel("Panel General de Turismo")
        self.titulo.setFont(QFont("Arial", 20))
        self.layout_general.addWidget(self.titulo)

        self.resumen_layout = QHBoxLayout()

        self.card_excursiones = self._crear_card("Excursiones")
        self.card_agencias = self._crear_card("Agencias")
        self.card_reservas = self._crear_card("Reservas")

        self.resumen_layout.addWidget(self.card_excursiones)
        self.resumen_layout.addWidget(self.card_agencias)
        self.resumen_layout.addWidget(self.card_reservas)

        self.layout_general.addLayout(self.resumen_layout)
        self.setLayout(self.layout_general)

        self.actualizar()

    def _crear_card(self, titulo):
        frame = QFrame()
        frame.setStyleSheet("""
            background-color: #f4f4f4;
            border-radius: 10px;
            padding: 20px;
        """)
        vbox = QVBoxLayout()

        label_titulo = QLabel(titulo)
        label_titulo.setFont(QFont("Arial", 14))
        label_cantidad = QLabel("0")
        label_cantidad.setFont(QFont("Arial", 24))

        vbox.addWidget(label_titulo)
        vbox.addWidget(label_cantidad)
        frame.setLayout(vbox)
        return frame

    def actualizar(self):
        self.card_excursiones.layout().itemAt(1).widget().setText(str(contar_excursiones()))
        self.card_agencias.layout().itemAt(1).widget().setText(str(contar_agencias()))
        self.card_reservas.layout().itemAt(1).widget().setText(str(contar_reservas()))
