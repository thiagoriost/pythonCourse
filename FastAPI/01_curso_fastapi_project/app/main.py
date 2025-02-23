from typing import Annotated
import zoneinfo
from datetime import datetime
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.db import create_all_tables
from app.routers import customers, transactions, invoices, plans


app = FastAPI(lifespan=create_all_tables) # Crea una instancia de la clase FastAPI
app.title = "My First FastAPI Project by RigoRiosH"
app.description = "This is a very simple project to practice FastAPI"
app.version = "0.0.1"
app.include_router(customers.router) # Incluye las rutas definidas en el archivo customers.py
app.include_router(transactions.router)
app.include_router(invoices.router)
app.include_router(plans.router)

@app.middleware("http") # Decorador que indica que la función se ejecutará como middleware
async def add_process_time_header(request: Request, call_next): # Función que recibe dos parámetros
    start_time = datetime.now() # Obtiene la hora actual
    response = await call_next(request) # Llama a la función call_next con el parámetro request
    process_time = datetime.now() - start_time # Calcula el tiempo de procesamiento
    response.headers["X-Process-Time"] = str(process_time) # Agrega el tiempo de procesamiento a las cabeceras de la respuesta
    print("process_time => ", f"Request: {request.url} completed in {process_time.microseconds} microseconds") # Imprime un mensaje con el tiempo de procesamiento
    return response # Retorna la respuesta

secuity = HTTPBasic() # Crea una instancia de la clase HTTPBasic

@app.get("/") # Decorador que indica que la función se ejecutará cuando se haga una petición GET a la ruta raíz
async def read_root(credentials: Annotated[HTTPBasicCredentials, Depends(secuity)]): # Función que recibe un parámetro credentials de tipo HTTPBasicCredentials
    print("credentials => ", credentials)
    if not credentials.username == "rigo" or not credentials.password == "rigo":
        raise HTTPException(status_code=401, detail="Unauthorized") # Lanza una excepción si las credenciales no son correctas
    return {"Hello": f"{credentials.username}"} # Retorna un diccionario con un mensaje de saludo

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
