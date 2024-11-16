import sys
from PyQt6.QtWidgets import QApplication, QtWidget


class VentanaVacia(QtWidget):

        def __init__(self):
                super().__init__(self)
                self.inicializarUI()

        def inicializarUI(self):
                self.setGeometry()