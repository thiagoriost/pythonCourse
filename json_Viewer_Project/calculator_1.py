import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLineEdit, QLabel
)
from PyQt5.QtCore import Qt

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurar ventana a pantalla completa
        self.setWindowTitle("Calculadora Básica")
        self.showMaximized()

        # Diseño principal
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Campo de entrada y etiqueta para mostrar resultados
        self.result_label = QLabel("Resultado: 0", self)
        self.result_label.setAlignment(Qt.AlignRight)
        self.result_label.setStyleSheet("font-size: 20px; padding: 10px;")
        self.layout.addWidget(self.result_label)

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Ingrese números separados por comas (ej. 5,10)")
        self.input_field.setStyleSheet("font-size: 16px; padding: 5px;")
        self.layout.addWidget(self.input_field)

        # Botones para operaciones
        self.buttons_layout = QHBoxLayout()

        self.add_button("Suma", self.calculate_sum)
        self.add_button("Resta", self.calculate_subtraction)
        self.add_button("Multiplicación", self.calculate_multiplication)
        self.add_button("División", self.calculate_division)

        self.layout.addLayout(self.buttons_layout)

    def add_button(self, label, function):
        """Crea un botón con una etiqueta y lo conecta a una función."""
        button = QPushButton(label, self)
        button.setStyleSheet("font-size: 16px; padding: 10px;")
        button.clicked.connect(function)
        self.buttons_layout.addWidget(button)

    def get_numbers(self):
        """Obtiene los números ingresados en el campo de entrada."""
        try:
            text = self.input_field.text()
            numbers = list(map(float, text.split(",")))  # Convertir texto a lista de números
            return numbers
        except ValueError:
            self.result_label.setText("Error: Ingrese números válidos separados por comas.")
            return None

    def calculate_sum(self):
        """Calcula la suma de los números ingresados."""
        numbers = self.get_numbers()
        if numbers:
            result = sum(numbers)
            self.result_label.setText(f"Resultado: {result}")

    def calculate_subtraction(self):
        """Calcula la resta de los números ingresados."""
        numbers = self.get_numbers()
        if numbers:
            result = numbers[0]
            for num in numbers[1:]:
                result -= num
            self.result_label.setText(f"Resultado: {result}")

    def calculate_multiplication(self):
        """Calcula la multiplicación de los números ingresados."""
        numbers = self.get_numbers()
        if numbers:
            result = 1
            for num in numbers:
                result *= num
            self.result_label.setText(f"Resultado: {result}")

    def calculate_division(self):
        """Calcula la división de los números ingresados."""
        numbers = self.get_numbers()
        if numbers:
            try:
                result = numbers[0]
                for num in numbers[1:]:
                    result /= num
                self.result_label.setText(f"Resultado: {result}")
            except ZeroDivisionError:
                self.result_label.setText("Error: División por cero no permitida.")

# Punto de entrada
if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
