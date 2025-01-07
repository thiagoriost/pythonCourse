""" Decoradores anidados """
# Decorador q comprueba el rol del empleado 
print("__1__")
def check_access(requiered_role):
    print("__2__")
    def decorator(my_funci):
        print("__4__")        
        def wraper(employee):
            print("__6__")            
            # valida si el rol del empleado coincide con el requerido
            if employee.get('role') == requiered_role:
                print("__7__1")
                return my_funci(employee)
            else:
                print("__7__")
                print(f"ACCESO DENEGADO, solo los {requiered_role} pueden hacerlo")       
        return wraper
    return decorator

def log_action(la_funcion):
    print("__3__")
    def wraper(employee):
        print("__8__")
        print(f'Registrando acción para el empleado {employee['name']}')
        return la_funcion(employee)
    return wraper


# se define para luego ser creado
@check_access('admin')
@log_action
def delete_employee(employee):
    print("__9__")
    print(f'El empleado {employee['name']}, ha sido eliminado')

print("__5__")

admin = { 'name': 'Carlos', 'role':'admin' }
employee = { 'name': 'Ana', 'role':'RRH' }

delete_employee(employee)
print("--------------------------")
delete_employee(admin)