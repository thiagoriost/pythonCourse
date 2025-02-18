from typing import Annotated
from fastapi import Depends, FastAPI
from sqlmodel import SQLModel, Session, create_engine

sqlite_name = "db.sqlite3" 
sqlite_url = f"sqlite:///{sqlite_name}" 

engine = create_engine(sqlite_url, echo=True) # Crea un motor de base de datos con la URL de la base de datos

def create_all_tables(app: FastAPI): # Función que crea la base de datos y las tablas
    SQLModel.metadata.create_all(engine) # Crea las tablas en la base de datos
    yield # Retorna un generador


def get_session(): # Función que retorna una sesión de la base de datos
    with Session(engine) as session: # Crea una sesión con el motor de la base de datos
        yield session # Retorna la sesión

SessionDep = Annotated[Session, Depends(get_session)] # Anotación que indica que la clase Session depende de la función get_session