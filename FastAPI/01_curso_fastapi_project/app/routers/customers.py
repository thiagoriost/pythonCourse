from fastapi import HTTPException
from fastapi import status, FastAPI, Depends, HTTPException, APIRouter, Response
from typing import List
from sqlmodel import select
from ..models import CustomerCreate, Customer, CustomerUpdate
from ..db import SessionDep, create_all_tables


router = APIRouter() # Crea una instancia de la clase APIRouter para definir rutas agrupadas en un archivo independiente de main.py 


# Simulación de base de datos en memoria
db: list[Customer] = []

@router.post("/custumers", response_model=Customer) # Decorador que indica que la función se ejecutará cuando se haga una petición post a la ruta /custumer
async def create_custumers(custumer: CustomerCreate, session: SessionDep): # Función que recibe un parámetro de tipo Customer
    print("custumer => ", custumer)
    # new_id = len(db) + 1
    # new_customer = Customer(id=new_id, **custumer.model_dump()) # Crea un objeto de la clase Customer con el id y los atributos del objeto custumer
    # db.append(new_customer)
    new_custumer = Customer.model_validate(custumer.model_dump()) # Crea un objeto de la clase Customer con los atributos del objeto custumer
    session.add(new_custumer) # Agrega el objeto new_custumer a la sesión
    session.commit() # Guarda los cambios en la base de datos
    session.refresh(new_custumer) # Actualiza el objeto new_custumer con los datos de la base de datos 
    return new_custumer

@router.get("/customers/", response_model=List[Customer])
async def get_customers(session: SessionDep):
    # return db
    return session.exec(select(Customer)).all()

@router.get("/customers/{customer_id}", response_model=Customer)
async def get_customers_by_id(customer_id:int, session: SessionDep):
    # return db
    # return session.exec(select(Customer).where(Customer.id == customer_id)).first()
    customer_db = session.get(Customer, customer_id) # Obtiene el objeto Customer con el id customer_id, q es otra forma de hacer la consulta anterior
    if not customer_db:
        # return {"error": "Customer not found"} # Retorna un diccionario con un mensaje de error si no se encuentra el cliente
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found BY RRHH") # Lanza una excepción si no se encuentra el cliente
    return customer_db

@router.patch("/customers/{customer_id}", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def edit_customers_by_id(customer_id:int, session: SessionDep, customer_data: CustomerUpdate):
    
    customer_db = session.get(Customer, customer_id) # Obtiene el objeto Customer con el id customer_id, q es otra forma de hacer la consulta anterior
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found BY RRHH") # Lanza una excepción si no se encuentra el cliente
    
    customer_data_dict = customer_data.model_dump(exclude_unset=True) # Crea un diccionario con los atributos del objeto customer_data
    customer_db.sqlmodel_update(customer_data_dict) # Actualiza los atributos del objeto customer_db con los del diccionario customer_data_dict
    session.add(customer_db) # Agrega el objeto customer_db a la sesión
    session.commit() # Guarda los cambios en la base de datos
    session.refresh(customer_db) # Actualiza el objeto customer_db con los datos de la base de datos
    return customer_db


@router.delete("/customers/{customer_id}")
async def delete_customers_by_id(customer_id:int, session: SessionDep):
    # return db
    # return session.exec(select(Customer).where(Customer.id == customer_id)).first()
    customer_db = session.get(Customer, customer_id) # Obtiene el objeto Customer con el id customer_id, q es otra forma de hacer la consulta anterior
    if not customer_db:
        # return {"error": "Customer not found"} # Retorna un diccionario con un mensaje de error si no se encuentra el cliente
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found BY RRHH") # Lanza una excepción si no se encuentra el cliente
    
    session.delete(customer_db) # Elimina el cliente de la base de datos
    session.commit() # Guarda los cambios en la base de datos

    return {"message": "Customer deleted"} # Retorna un diccionario con un mensaje de éxito si se elimina el cliente
