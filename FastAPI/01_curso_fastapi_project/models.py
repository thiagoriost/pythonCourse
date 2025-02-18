from fastapi import FastAPI
from pydantic import BaseModel 
from sqlmodel import Field, SQLModel # Importación de las clases Field y SQLModel de SQLModel



# creacion de un modelo
class CustumerBase(SQLModel): # Clase que hereda de BaseModel
    # id: int
    name: str = Field(default=None) # Atributo name de tipo str
    description: str | None = Field(default=None) # Atributo description de tipo str o None
    email: str = Field(default=None) # Atributo email de tipo str
    age: int = Field(default=None) # Atributo age de tipo int

class Custumer(CustumerBase, table=True): # Clase que hereda de CustumerBase..
    id: int | None = Field(default=None, primary_key=True) # Atributo id de tipo int o None con valor por defecto None y clave primaria

    # class Config: # Clase Config
    #     orm_mode = True # Indica que la clase es un modelo de ORM

class CusomerCreate(CustumerBase):
    pass # No se añade nada nuevo a la clase

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