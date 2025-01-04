class Vehicle:
    def __init__(self, brand, model, price):
        # encapsulacion
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True
        
    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El carro {self.brand}. Ha sido vendido")
        else:
            print(f"El vehiculo {self.brand}. No esta disponible")
    
    # Abastraccion
    def check_available(self):
        return self.is_available
    
    # Abastraccion
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por las subclases")
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por las subclases")
    
# hereda de la clase vehiculo
class Car(Vehicle):
    # poliformismo
    def start_engine(self):
        if not self.is_available:
            return f"El motor del vehiculo {self.brand} esta en marcha"
        else:
            return f"El coche {self.brand} no esta disponible"

    # poliformismo
    def stop_engine(self):
        if self.is_available:
            return f"El motor del coche {self.brand} se ha detenido"
        else:
            return f"El coche {self.brand} no esta disponible"

class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"the Bike {self.brand} is run"
        else:
            return f"The bike {self.brand} is not avalibable"
        
    def stop_engine(self):
        if self.is_available:
            return f"the Bike {self.brand} is stop"
        else:
            return f"The bike {self.brand} is not avalibable"
        
class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del camion {self.brand} esta en marcha"
        else:
            return f"El camion {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"El motor del camion {self.brand} se ha detenido"
        else:
            return f"El camion {self.brand} no esta disponible"
        
class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []
        
    def buy_vehicule(self, vehicule: Vehicle):
        if vehicule.check_available():
            vehicule.sell()
            self.purchased_vehicles.append(vehicule)
        else:
            print(f"Sorry, {vehicule.brand} no esta disponible")
    
    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availability = "Disponible"
        else:
            availability = "No disponible"
        print(f"El {vehicle.brand} esta {availability} y cuesta {vehicle.get_price()}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []
    
    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido añadido al inventario")
        
    def register_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f"El {customer.name} ha sido registrado")
    
    def show_available_vehicles(self):
        print(f"Vehiculos disponibles en la tienda")
        for vehi in self.inventory:
            if vehi.check_available():
                print(f"-- {vehi.brand} por {vehi.get_price()}")
        
car1 = Car("Toyota", "Corola", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Carlos")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)
# mostrar vehiculos disponibles
dealership.show_available_vehicles()
# Cliente consultar vehiculo
customer1.inquire_vehicle(car1)
customer1.inquire_vehicle(bike1)
customer1.inquire_vehicle(truck1)
# cliente compra un vehiculo
customer1.buy_vehicule(bike1)
# mostrar vehiculos disponibles
dealership.show_available_vehicles()