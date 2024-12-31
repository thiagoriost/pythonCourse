import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
from PyQt5.QtGui import QColor

# Clase principal de la ventana
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración inicial de la ventana
        self.setWindowTitle("Hello World PyQt")
        self.setGeometry(100, 100, 400, 300)

        # Etiqueta principal
        label = QLabel("¡Hola Mundo!", self)
        label.setGeometry(50, 10, 100, 10)
        # label.backgroundRole('red')

        # Botón 1: Muestra mensaje en la consola
        button_message = QPushButton("Mostrar Mensaje", self)
        button_message.setGeometry(50, 200, 150, 30)
        button_message.clicked.connect(self.show_message)

        # Botón 2: Cambia el color de fondo
        button_color = QPushButton("Cambiar Color", self)
        button_color.setGeometry(220, 200, 150, 30)
        button_color.clicked.connect(self.change_background_color)

    def show_message(self):
        print("¡Botón 'Mostrar Mensaje' presionado!")

    def change_background_color(self):
        # Generar un color aleatorio en formato RGB
        random_color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # Aplicar el color como fondo usando estilos
        self.setStyleSheet(f"background-color: {random_color.name()};")

# Punto de entrada
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
