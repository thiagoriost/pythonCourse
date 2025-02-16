import zoneinfo
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from models import Custumer, Transaction, Invoice


app = FastAPI()

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

@app.post("/custumers") # Decorador que indica que la función se ejecutará cuando se haga una petición post a la ruta /custumer
async def create_custumers(custumer: Custumer): # Función que recibe un parámetro de tipo Custumer
    print("custumer => ", custumer)
    return custumer # Retorna el objeto custumer

@app.post("/transactions") # Decorador que indica que la función se ejecutará cuando se haga una petición post a la ruta /custumer
async def create_transactions(transaction: Transaction): # Función que recibe un parámetro de tipo Custumer
    print("transaction => ", transaction)
    return transaction # Retorna el objeto custumer

@app.post("/invoices") # Decorador que indica que la función se ejecutará cuando se haga una petición post a la ruta /custumer
async def create_invoices(invoice: Invoice): # Función que recibe un parámetro de tipo Custumer
    print("invoice => ", invoice)
    return invoice # Retorna el objeto custumer