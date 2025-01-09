import reports
 
""" Generar reortes de ventas y gastos usando funciones del modulo """
sales_report = reports.generate_sales_report('October', 10000)
expense_reort = reports.generate_expenses_report('October', 5000)

print(f"sales_report => ", sales_report)
print(f"expense_reort => ", expense_reort)