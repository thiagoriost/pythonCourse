import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton

# Clase principal de la ventana
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World PyQt--")
        self.setGeometry(100, 100, 400, 300)  # Posición x, y, ancho, alto

        label = QLabel("¡Hola Mundo!", self)  # Texto principal
        label.setGeometry(150, 130, 200, 30)  # Posición y tamaño del texto
        
        button = QPushButton("Clic aquí", self)
        button.setGeometry(150, 200, 100, 30)
        button.clicked.connect(lambda: print("¡Botón presionado!"))
        
        self.setStyleSheet("background-color: lightblue;")

# Punto de entrada
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crear aplicación
    window = MainWindow()         # Crear ventana principal
    window.show()                 # Mostrar la ventana
    sys.exit(app.exec())          # Ejecutar el evento principal
