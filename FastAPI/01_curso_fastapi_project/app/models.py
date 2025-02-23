from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, field_validator
from sqlmodel import Field, Relationship, SQLModel, Session, select # Importación de las clases Field y SQLModel de SQLModel
from app.db import engine # Importación del motor engine


class StatusEnum(str, Enum): # Clase StatusEnum que hereda de Enum
    ACTIVE = "active" # Atributo ACTIVE con valor "active"
    INACTIVE = "inactive" # Atributo INACTIVE con valor "inactive"

class CustomerPlan(SQLModel, table=True): # Clase que hereda de SQLModel
    id: int | None = Field(default=None, primary_key=True) # Atributo id de tipo int o None con valor por defecto None y clave primaria
    plan_id: int = Field(foreign_key="plan.id") # Atributo plan_id de tipo int con clave foránea a la tabla plan y campo id de la tabla plan 
    customer_id: int = Field(foreign_key="customer.id") # Atributo customer_id de tipo int con clave foránea a la tabla customer y campo id de la tabla customer
    status: StatusEnum = Field(default=StatusEnum.ACTIVE) # Atributo status de tipo StatusEnum con valor por defecto StatusEnum.ACTIVE

class Plan(SQLModel, table=True): # Clase que hereda de SQLModel
    id: int | None = Field(default=None, primary_key=True) # Atributo id de tipo int con valor por defecto None y clave primaria
    name: str = Field(default=None) # Atributo name de tipo str con valor por defecto None
    price: float = Field(default=None) # Atributo price de tipo float con valor por defecto None
    description: str | None = Field(default=None) # Atributo description de tipo str o None con valor por defecto None
    customers: list["Customer"] = Relationship(  # Atributo customers de tipo lista de Customer con relación one to many
            back_populates="plans", # Atributo back_populates con el nombre del atributo de la clase Customer que establece la relación inversa 
            link_model=CustomerPlan # Atributo link_model con el modelo CustomerPlan 
        )
        


# creacion de un modelo
class CustomerBase(SQLModel): # Clase que hereda de BaseModel
    # id: int
    name: str = Field(default=None) # Atributo name de tipo str
    description: str | None = Field(default=None) # Atributo description de tipo str o None
    email: EmailStr = Field(default=None) # Atributo email de tipo EmailStr con valor por defecto None 
    age: int = Field(default=None) # Atributo age de tipo int

    @field_validator("email") # Decorador que indica que el método es un validador de campo
    def validate_email(cls, value): # Método que recibe un parámetro v
        session = Session(engine) # Crea una instancia de la clase Session con el motor engine
        query = select(Customer).where(Customer.email == value) # Crea una consulta para obtener los clientes con el email v
        result = session.exec(query).first() # Ejecuta la consulta y obtiene el primer resultado
        if result: # Si result es verdadero
            raise ValueError("Email already exists") # Lanza una excepción con el mensaje "Email already exists"
        return value # Retorna el valor v

class Customer(CustomerBase, table=True): # Clase que hereda de CustomerBase..
    id: int | None = Field(default=None, primary_key=True) # Atributo id de tipo int o None con valor por defecto None y clave primaria
    transactions: list["Transaction"] = Relationship(back_populates="customer") # Atributo transactions de tipo lista de Transaction con relación many to one
    plans: list[Plan] = Relationship(back_populates="customers", link_model=CustomerPlan) # Atributo plans de tipo lista de Plan con relación one to many

    # class Config: # Clase Config
    #     orm_mode = True # Indica que la clase es un modelo de ORM

class CustomerCreate(CustomerBase):
    pass # No se añade nada nuevo a la clase

class CustomerUpdate(CustomerBase):
    pass # No se añade nada nuevo a la clase

class TransactionBase(SQLModel):
    amount: float
    description: str | None
    # date: str | None

class TransactionCreate(TransactionBase):
    customer_id: int = Field(foreign_key="customer.id") # Atributo customer_id de tipo int con clave foránea a la tabla customer y campo id de la tabla customer 

class Transaction(TransactionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    customer_id: int = Field(default=None, foreign_key="customer.id")
    customer: Customer = Relationship(back_populates="transactions") # Atributo customer de tipo Customer con relación one to many

class Invoice(BaseModel):
    id: int
    customer: Customer
    transaction: list[Transaction]
    total: int

    @property # Decorador que indica que el método es una propiedad
    def ammount_total(self):
        return sum(transaction.amount for transaction in self.transaction) # Retorna la suma de los montos de las transacciones de la factura