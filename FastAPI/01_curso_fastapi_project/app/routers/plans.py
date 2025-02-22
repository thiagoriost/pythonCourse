from fastapi import APIRouter
from sqlmodel import select
from app.models import Plan
from app.db import SessionDep

router = APIRouter() # Crea una instancia de la clase APIRouter para definir rutas agrupadas en un archivo independiente de main.py

@router.post("/plans", response_model=Plan, status_code=201, tags=['plans'])
def create_plan(plan_data:Plan, session:SessionDep):
    plan_db = Plan.model_validate(plan_data.model_dump()) # Crea un objeto de la clase Plan con los atributos del diccionario plan_data.model_dump()
    session.add(plan_db)
    session.commit()
    session.refresh(plan_db)
    return plan_db

@router.get("/plans", response_model=list[Plan], tags=['plans'])
def get_plans(session:SessionDep):
    query = session.exec(select(Plan))
    return query.all()