# import calcularSumaTodasCompras.my_functions as aa 
import pkg.my_functions as my_functions


def get_total(orders):
  # Tu código aquí 👇
  resp = my_functions.get_totals(orders)
  totals = my_functions.calc_total(resp)
  return totals

orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

total = get_total(orders)
print(total)