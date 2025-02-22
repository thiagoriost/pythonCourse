from fastapi import HTTPException, Query
from fastapi import status, HTTPException, APIRouter, Response
from typing import List
from sqlmodel import select
from ..models import CustomerCreate, Customer, CustomerPlan, CustomerUpdate, Plan, StatusEnum
from ..db import SessionDep
# from app.db import SessionDep


router = APIRouter() # Crea una instancia de la clase APIRouter para definir rutas agrupadas en un archivo independiente de main.py 


# Simulación de base de datos en memoria
db: list[Customer] = []

@router.post("/custumers", response_model=Customer, tags=['customers']) # Decorador que indica que la función se ejecutará cuando se haga una petición post a la ruta /custumer
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

@router.get("/customers/", response_model=List[Customer], tags=['customers'])
async def get_customers(session: SessionDep):
    # return db
    return session.exec(select(Customer)).all()

@router.get("/customers/{customer_id}", response_model=Customer, tags=['customers'])
async def get_customers_by_id(customer_id:int, session: SessionDep):
    # return db
    # return session.exec(select(Customer).where(Customer.id == customer_id)).first()
    customer_db = session.get(Customer, customer_id) # Obtiene el objeto Customer con el id customer_id, q es otra forma de hacer la consulta anterior
    if not customer_db:
        # return {"error": "Customer not found"} # Retorna un diccionario con un mensaje de error si no se encuentra el cliente
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found BY RRHH") # Lanza una excepción si no se encuentra el cliente
    
    return customer_db

@router.patch("/customers/{customer_id}", response_model=Customer, tags=['customers'], status_code=status.HTTP_201_CREATED)
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


@router.delete("/customers/{customer_id}", tags=['customers'])
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

@router.post("/customers/{customer_id}/plans/{plan_id}", tags=['customers'])
async def add_plan_to_customer(customer_id:int, plan_id:int, session: SessionDep, plan_status:StatusEnum = Query()):
    customer_db = session.get(Customer, customer_id) # Obtiene el objeto Customer con el id customer_id del diccionario transaction_data_dict 
    plan_db = session.get(Plan, plan_id) # Obtiene el objeto Plan con el id plan_id del diccionario transaction_data_dict 
    if not customer_db or not plan_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer or Plan not found")
    customer_plan_db = CustomerPlan(plan_id=plan_db.id, customer_id=customer_db.id, status=plan_status) # Crea un objeto de la clase CustomerPlan con los ids de los objetos customer_db y plan_db 
    session.add(customer_plan_db)
    session.commit()
    session.refresh(customer_plan_db)
    return customer_plan_db

@router.get("/customers/{customer_id}/plans/", tags=['customers'])
async def subscribe_customer_to_plan(customer_id:int, session: SessionDep):
    customer_db = session.get(Customer, customer_id) # Obtiene el objeto Customer con el id customer_id del diccionario transaction_data_dict 
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found") 
    return customer_db.plans

@router.get("/customers/{customer_id}/plans/", tags=['customers'])
async def actives_plan(customer_id:int, session: SessionDep, plan_status:StatusEnum = Query()):
    customer_db = session.get(Customer, customer_id) # Obtiene el objeto Customer con el id customer_id del diccionario transaction_data_dict 
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found") 
    
    query = (
        select(CustomerPlan) # Crea una consulta para obtener los planes activos del cliente con el id customer_id del diccionario transaction_data_dict 
        .where(CustomerPlan.customer_id == customer_id) 
        .where(CustomerPlan.status == plan_status) 
    ) # Crea una consulta para obtener los planes activos del cliente con el id customer_id del diccionario transaction data_dict 
    plans = session.exec(query).all() # Obtiene los planes activos del cliente con el id customer_id del diccionario transaction_data_dict 
    return plans