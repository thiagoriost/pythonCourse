from pydantic import BaseModel



# creacion de un modelo
class Custumer(BaseModel): # Clase que hereda de BaseModel
    id: int
    name: str # Atributo name de tipo str
    description: str | None # Atributo description de tipo str o None
    email: str # Atributo email de tipo str
    age: int # Atributo age de tipo int

class Transaction(BaseModel):
    id: int
    amount: float
    description: str | None
    # date: str | None
    # custumer: Custumer | None

class Invoice(BaseModel):
    id: int
    customer: Custumer
    transaction: list[Transaction]
    total: int

    @property # Decorador que indica que el método es una propiedad
    def ammount_total(self):
        return sum(transaction.amount for transaction in self.transaction) # Retorna la suma de los montos de las transacciones de la factura