admin= {
    'name': 'Carlos',
    'role':'admin'
}
employ = {
    'Ana': 'Carlos',
    'role':'RRH'
}

def check_access(my_funtion):
    def wraper(employee):
        # comprueba el rol de administrador
        if employee.get('role') == 'admin':
            print("Permisos ok")            
            return my_funtion(employee)
        else:
            print("ACCESO DENEGADO, solo los administradores pueden acceder")
    return wraper

print("---------")
@check_access
def delelte_employee(employee):
    print(f'El empleado {employee['name']}, ha sido eliminado')

delelte_employee(employ)
print("---------")
delelte_employee(admin)
print("---------")