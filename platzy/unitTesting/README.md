1. Se emplea unittest
2. Se debe declarar la clase de este modo
###    class CalculatorTests(unittest.TestCase):
3. Cada prueba se configura en un metodo, el cual su nombre debe empezar con la palabra "test_.." asi:
###  def test_sum(self):
4. para correr las pruebas se debe ubicar en donde se encuentra la carpeta que contienn las pruebas y ejecutar el siguiente comando:
### python -m unittest discover -v -s [nombre de la carpeta que contiene los .py de pruebas]
