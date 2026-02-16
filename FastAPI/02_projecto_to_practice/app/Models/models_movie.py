import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, HttpUrl


class Model_base_Movie(BaseModel):
    title: str = Field(min_length=5, max_length=30, default='My Movie') # validaciones
    overview: str = Field(min_length=15, max_length=50, default='A Movie descriptions')
    categories: List[str] = Field(..., min_items=1)  # Lista con al menos un elemento
    year: int = Field(
        le=datetime.date.today().year,  # Año menor o igual al actual
        ge=1900,  # Año mayor o igual a 1900
        default= datetime.date.today().year
    )
    rating: float = Field(ge=0, le=10)  # Rango entre 0 y 10
    poster_path: HttpUrl  # Validación para asegurar que sea una URL válida

    model_config = {
        'json_schema_extra':{
            'example':{
                'categories': ['Drama'],
                'id':1,
                'overview': 'A Movie descriptions',
                'poster_path': 'https://example.com/poster.jpg',
                'rating': 0.9,
                'title': 'My Movie',
                'year': 2025,

            }
        }
    }

class Model_MovieUpDate(Model_base_Movie):
    pass

class Movie_model(Model_base_Movie):
    # id: int | None = None
    id: Optional[int] = None    

class Model_Movie_Create(Model_MovieUpDate):
    id: int    


