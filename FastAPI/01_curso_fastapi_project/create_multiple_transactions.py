from sqlmodel import Session
from app.db import engine
from app.models import Transaction, Customer

sesion = Session(engine)
customer = Customer(
    name = "Juan",
    email = "hola@sdf.com",
    age = 20,
    description = "Hola mundo"
)
sesion.add(customer)
sesion.commit()
sesion.refresh(customer)

for custorX in range(100):
    sesion.add(Transaction(
        customer_id = customer.id,
        description=f"Test number {custorX}",
        amount=100.0
    ))
sesion.commit()