from typing import List
import zoneinfo
from datetime import datetime
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from sqlmodel import select
from models import CusomerCreate, Custumer, Transaction, Invoice
from db import SessionDep, create_all_tables


app = FastAPI(lifespan=create_all_tables) # Crea una instancia de la clase FastAPI

@app.get("/") # Decorador que indica que la función se ejecutará cuando se haga una petición GET a la ruta raíz
async def read_root():
    return {"Hello": "World2"} # Retorna un diccionario con un mensaje de saludo

country_timezones = {
    "US": "America/New_York",
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima"
}

@app.get("/time/{iso_code}") # Decorador que indica que la función se ejecutará cuando se haga una petición GET a la ruta /time
async def time(iso_code: str): # La función recibe un parámetro iso_code de tipo str
    print("iso_code => ", iso_code)
    iso = iso_code.upper() # Convierte el iso_code a mayúsculas
    timezone_str = country_timezones.get(iso) # Obtiene la zona horaria del país correspondiente al iso_code
    print("timezone_str => ", timezone_str)

    tz = zoneinfo.ZoneInfo(timezone_str) # Crea un objeto de la clase ZoneInfo con la zona horaria

    return {"time": datetime.now(tz)} # Retorna un diccionario con la hora actual en la zona horaria correspondiente al país del iso_code


# Simulación de base de datos en memoria
db: list[Custumer] = []

@app.post("/custumers", response_model=Custumer) # Decorador que indica que la función se ejecutará cuando se haga una petición post a la ruta /custumer
async def create_custumers(custumer: CusomerCreate, session: SessionDep): # Función que recibe un parámetro de tipo Custumer
    print("custumer => ", custumer)
    # new_id = len(db) + 1
    # new_customer = Custumer(id=new_id, **custumer.model_dump()) # Crea un objeto de la clase Custumer con el id y los atributos del objeto custumer
    # db.append(new_customer)
    new_custumer = Custumer.model_validate(custumer.model_dump()) # Crea un objeto de la clase Custumer con los atributos del objeto custumer
    session.add(new_custumer) # Agrega el objeto new_custumer a la sesión
    session.commit() # Guarda los cambios en la base de datos
    session.refresh(new_custumer) # Actualiza el objeto new_custumer con los datos de la base de datos 
    return new_custumer

@app.get("/customers/", response_model=List[Custumer])
async def get_customers(session: SessionDep):
    # return db
    return session.exec(select(Custumer)).all()

@app.get("/customers/{customer_id}", response_model=Custumer)
async def get_customers_by_id(customer_id:int, session: SessionDep):
    # return db
    # return session.exec(select(Custumer).where(Custumer.id == customer_id)).first()
    customer_db = session.get(Custumer, customer_id) # Obtiene el objeto Custumer con el id customer_id, q es otra forma de hacer la consulta anterior
    if not customer_db:
        # return {"error": "Customer not found"} # Retorna un diccionario con un mensaje de error si no se encuentra el cliente
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found BY RRHH") # Lanza una excepción si no se encuentra el cliente
    return customer_db

@app.delete("/customers/{customer_id}")
async def delete_customers_by_id(customer_id:int, session: SessionDep):
    # return db
    # return session.exec(select(Custumer).where(Custumer.id == customer_id)).first()
    customer_db = session.get(Custumer, customer_id) # Obtiene el objeto Custumer con el id customer_id, q es otra forma de hacer la consulta anterior
    if not customer_db:
        # return {"error": "Customer not found"} # Retorna un diccionario con un mensaje de error si no se encuentra el cliente
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found BY RRHH") # Lanza una excepción si no se encuentra el cliente
    
    session.delete(customer_db) # Elimina el cliente de la base de datos
    session.commit() # Guarda los cambios en la base de datos

    return {"message": "Customer deleted"} # Retorna un diccionario con un mensaje de éxito si se elimina el cliente

@app.post("/transactions") # Decorador que indica que la función se ejecutará cuando se haga una petición post a la ruta /custumer
async def create_transactions(transaction: Transaction): # Función que recibe un parámetro de tipo Custumer
    print("transaction => ", transaction)
    return transaction # Retorna el objeto custumer

@app.post("/invoices") # Decorador que indica que la función se ejecutará cuando se haga una petición post a la ruta /custumer
async def create_invoices(invoice: Invoice): # Función que recibe un parámetro de tipo Custumer
    print("invoice => ", invoice)
    return invoice # Retorna el objeto custumer