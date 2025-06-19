import sys
import os

# 🆕 Crear DB si no existe
from init_db import crear_tabla_excursiones, crear_tabla_agencias, crear_tabla_reservas

if not os.path.exists("turismo.db"):
    crear_tabla_excursiones()
    crear_tabla_agencias()
    crear_tabla_reservas()

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

from widgets.dashboard import DashboardWidget
from widgets.form_agencia import FormAgenciaWidget
from widgets.form_excursion import FormExcursionWidget
from widgets.form_reserva import FormReservaWidget
from widgets.listado_reserva import ListadoReservasWidget
from PyQt5.QtWidgets import QMainWindow, QWidget, QStackedWidget, QHBoxLayout, QListWidget, QListWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRM de Turismo - Ushuaia")
        self.setMinimumSize(1000, 700)

        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.sidebar = QListWidget()
        self.sidebar.setIconSize(QSize(24, 24))
        self.sidebar.setFixedWidth(200)
        self.sidebar.setStyleSheet("background-color: #2e3b4e; color: white; font-size: 14px;")
        self.sidebar.addItem(QListWidgetItem(QIcon(), "Dashboard"))
        self.sidebar.addItem(QListWidgetItem(QIcon(), "Alta Agencia"))
        self.sidebar.addItem(QListWidgetItem(QIcon(), "Alta Excursión"))
        self.sidebar.addItem(QListWidgetItem(QIcon(), "Registrar Reserva"))
        self.sidebar.addItem(QListWidgetItem(QIcon(), "Listado de Reservas"))
        self.sidebar.currentRowChanged.connect(self.display_view)

        self.stack = QStackedWidget()
        self.views = [
            DashboardWidget(),
            FormAgenciaWidget(),
            FormExcursionWidget(),
            FormReservaWidget(),
            ListadoReservasWidget()
        ]
        for view in self.views:
            self.stack.addWidget(view)

        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.stack, 1)
        self.sidebar.setCurrentRow(0)

    def display_view(self, index):
        self.stack.setCurrentIndex(index)
        if index == 0:
            self.views[0].actualizar()
        elif index == 3:
            self.views[3].actualizar()


def main():
    app = QApplication(sys.argv)

    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    qss_path = os.path.join(base_path, "estilos", "style.qss")
    with open(qss_path, "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
