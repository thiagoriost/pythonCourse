from sqlmodel import select
from app.models import Customer, Transaction, TransactionCreate
from app.db import SessionDep


from fastapi import APIRouter, HTTPException, Query, status


router = APIRouter() # Crea una instancia de la clase APIRouter para definir rutas agrupadas en un archivo independiente de main.py 


@router.post("/transactions", status_code=status.HTTP_201_CREATED , tags=['transactions']) # Decorador que indica que la función se ejecutará cuando se haga una petición post a la ruta /custumer
async def create_transactions(transaction: TransactionCreate, session: SessionDep): # Función que recibe un parámetro de tipo Customer
    print("transaction => ", transaction)
    transaction_data_dict = transaction.model_dump() # Crea un diccionario con los atributos del objeto transaction 
    customer = session.get(Customer, transaction_data_dict["customer_id"]) # Obtiene el objeto Customer con el id customer_id del diccionario transaction_data_dict 
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    transaction_db =  Transaction.model_validate(transaction_data_dict) # Crea un objeto de la clase Transaction con los atributos del diccionario transaction_data_dict 
    session.add(transaction_db) # Agrega el objeto transaction_db a la sesión
    session.commit() # Guarda los cambios en la base de datos
    session.refresh(transaction_db) # Actualiza el objeto transaction_db con los datos de la base de datos
    return transaction_db # Retorna el objeto transaction_db

@router.get("/transactions/", tags=['transactions'])
async def get_transactions(session: SessionDep, 
                           skip: int = Query(0, description="Registros a omitir"), 
                           limit: int = Query(10, description="Numero de registros")): # Función que recibe un parámetro de tipo SessionDep y dos parámetros opcionales de tipo int 
    query = select(Transaction).offset(skip).limit(limit) # Crea una consulta para obtener los objetos de la clase Transaction con un límite y un offset
    transac = session.exec(query).all() # Ejecuta la consulta y obtiene todos los objetos de la clase Transaction de la base de datos 
    return transac