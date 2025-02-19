from typing import List
import zoneinfo
from datetime import datetime
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from sqlmodel import select
from ..models import CustomerCreate, Customer, Transaction, Invoice, CustomerUpdate
from ..db import SessionDep, create_all_tables


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



@app.post("/transactions") # Decorador que indica que la función se ejecutará cuando se haga una petición post a la ruta /custumer
async def create_transactions(transaction: Transaction): # Función que recibe un parámetro de tipo Customer
    print("transaction => ", transaction)
    return transaction # Retorna el objeto custumer

@app.post("/invoices") # Decorador que indica que la función se ejecutará cuando se haga una petición post a la ruta /custumer
async def create_invoices(invoice: Invoice): # Función que recibe un parámetro de tipo Customer
    print("invoice => ", invoice)
    return invoice # Retorna el objeto custumer