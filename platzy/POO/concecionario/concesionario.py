class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_avalaible = True
        
    
    def sell(self):
        if self.is_avalaible:
            self.is_avalaible = False
            print(f"Carro {self.brand} vendido")
        else:
            print(f"Carro {self.brand} no esta disponible")
    
    def check_availability(self):
        return self.is_avalaible
    
    def get_price(self):
        return self.price
            
class Customer:
    def __init__(self, name):
        self.name = name
        self.cars_purchased = []
    
    def buy_car(self, car):
        if car.check_availability():
            car.sell()
            self.cars_purchased.append(car)
        else:
            print(f"Sorry, {car.brand} {car.model} is not availabable")
    
    def inquire_car(self, car):
        availability = "disponible" if car.check_availability() else "No disponible"
        print(f"El coche {car.brand} {car.model} esta {availability} y cuesta {car.price}")
        
class DealerShip:
    def __init__(self):
        self.inventory = []
        self.customers = []
    
    def add_car(self, car):
        self.inventory.append(car)
        print(f"El coche {car.brand} {car.model} ha sido agregado al inventario")
    
    def register_customer(self, customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido registrado")
        
    def show_available_cars(self):
        print(f"Coches disponibles en la concesionaria")
        for car in self.inventory:
            if car.check_availability():
                print(f"- {car.brand} {car.model} por {car.get_price()}")

car1 = Car("Toyota", "Corola", 20000)
car2 = Car("Honda", "Civic", 22000)
car3 = Car("Ford", "Mistang", 35000)

customer1 = Customer("Carlos")

dealerShip = DealerShip()
dealerShip.add_car(car1)
dealerShip.add_car(car2)
dealerShip.add_car(car3)
dealerShip.register_customer(customer1)

dealerShip.show_available_cars()
customer1.inquire_car(car1)
customer1.buy_car(car2)
dealerShip.show_available_cars()
customer1.buy_car(car2)
dealerShip.show_available_cars()
