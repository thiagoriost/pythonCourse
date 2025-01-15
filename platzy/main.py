from PAQUETES.pkg.mod_1 import func_1, func_2
from PAQUETES.pkg.mod_2 import func_3, func_4

print("func_1 => ", func_1())
print("func_2 => ", func_2())
print("func_3 => ", func_3())
print("func_4 => ", func_4())

import PAQUETES.pkg as pk
import PAQUETES.pkg.mod_1 as mod1
print("URL => ", pk.URL)
print("mod1.func_1 => ", mod1.func_1())
