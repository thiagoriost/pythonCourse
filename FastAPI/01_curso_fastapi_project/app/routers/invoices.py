from app.models import Invoice
from fastapi import APIRouter


router = APIRouter() # Crea una instancia de la clase APIRouter para definir rutas agrupadas en un archivo independiente de main.py 

@router.post("/invoices", tags=['invoices']) # Decorador que indica que la función se ejecutará cuando se haga una petición post a la ruta /custumer
async def create_invoices(invoice: Invoice): # Función que recibe un parámetro de tipo Customer
    print("invoice => ", invoice)
    return invoice # Retorna el objeto custumer