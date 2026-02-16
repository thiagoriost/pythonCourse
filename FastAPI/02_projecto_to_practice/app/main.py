from typing import List
from fastapi import Body, FastAPI, HTTPException, Path, Query, status
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, FileResponse
from app.Models.models_movie import Model_Movie_Create, Model_MovieUpDate, Movie_model

app = FastAPI() 
app.title = "My First FastAPI Project by RigoRiosH"
app.description = "This is a very simple project to practice FastAPI"
app.version = "0.0.1"


data_movies = [
    {
        "id": 1,
        "title": "The Shawshank Redemption",
        "overview": "Two imprisoneddd",
        "categories": ["Drama"],
        "year": 1994,
        "rating": 9.3,
        "poster_path": "https://image.tmdb.org/t/p/w500/9O7gLzmreU0nGkIB6K3BsJbzvNv.jpg"
    },
    {
        "id": 2,
        "title": "The Godfather",
        "overview": "Spanning the years 1945 to 1955",
        "categories": ["Drama", "Crime"],
        "year": 1972,
        "rating": 9.2,
        "poster_path": "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg"
    },
    {
        "id": 3,
        "title": "The Dark Knight",
        "overview": "Batman raises the stakes in his war on crime",
        "categories": ["Drama", "Action", "Crime"],
        "year": 2008,
        "rating": 9.0,
        "poster_path": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg"
    }
]

def get_movie_by_id(data_movies: List[Movie_model], movie_id:int)-> Movie_model:

    for movie in data_movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found") 

def get_movie_by_category_and_year(data_movies: List[Movie_model], category:str, year:int)-> Movie_model:
    category = category.lower()
    for movie_item in data_movies:
        print("movie_item => ", movie_item)
        if category in [cat.lower() for cat in movie_item["categories"]] and movie_item["year"] == year:
            return movie_item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found") 

@app.get("/", tags=["Home"])
def home():
    # return HTMLResponse(content="<h1>Welcome to my first FastAPI project</h1>", status_code=200)
    return PlainTextResponse(content='Home')

@app.get("/movies", tags=["movies"], status_code=200, response_description="ejercicio de respuesta RRH, lo q debe devolver, 'Succes'") # Cambio de codigo de estado a 500 Internal server error 
def get_movies() -> List[Movie_model]:
    # return {"Hello": "World!!!!"}
    return JSONResponse(content=data_movies, status_code=200) # Devuelve la lista de peliculas en formato JSON con un codigo de estado 200 OK

@app.get("/get_file", tags=["movies"])
def get_file() -> FileResponse:
    file_path = "app/assets/diploma-fastapi.pdf"  # Ruta al archivo PDF
    return FileResponse(file_path, media_type="application/pdf", filename="diploma-fastapi.pdf", status_code=200)

@app.get("/movies/{id}", tags=["movies"])
def moviesByID(id: int = Path(gt=0))-> Movie_model:
    movie = get_movie_by_id(data_movies, id)
    return JSONResponse(content=movie)

@app.get("/movies/", tags=["movies"])
def moviesByCategory(year:int, category: str = Query(min_length=5, max_length=20))-> Movie_model:
    movie = get_movie_by_category_and_year(data_movies, category, year)
    return JSONResponse(content=movie)

@app.post("/movies", tags=['movies'])
def create_movie(
    id: int = Body(), 
    title: str = Body(), 
    overview: str = Body(), 
    categories: str = Body(), 
    year: int = Body(), 
    rating: float = Body(), 
    poster_path: str = Body()
    )-> List[Movie_model]:
    data_movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "categories": [categories],
        "year": year,
        "rating": rating,
        "poster_path": poster_path
    })
    # return JSONResponse(content=data_movies)
    return RedirectResponse('/movies', status_code=303)

@app.post("/movies2", tags=['movies'])
def create_movie_from_model(movie_model: Model_Movie_Create) -> List[Movie_model]:
    print("movie_model => ", movie_model)
    data_movies.append(movie_model.model_dump())
    return JSONResponse(content=data_movies)

# actualizacion
@app.put('/movies/{id}', tags=['movies'])
def update_movies(
    id: int,
    title: str = Body(), 
    overview: str = Body(), 
    categories: str = Body(), 
    year: int = Body(), 
    rating: float = Body(), 
    poster_path: str = Body()
)-> List[Movie_model]:
    for movie in data_movies:
        if movie['id'] == id:
            movie['title'] = title
            movie['overview'] = overview
            movie['categories'] = [categories]
            movie['year'] = year
            movie['rating'] = rating
            movie['poster_path']    = poster_path
    return JSONResponse(content= data_movies)

# actualizacion
@app.put('/movies2/{id}', tags=['movies'])
def update_movies_from_model(id: int, model_MovieUpDate: Model_MovieUpDate)-> List[Movie_model]:
    for mov in data_movies:
        if mov['id'] == id:
            mov['title'] = model_MovieUpDate.title
            mov['overview'] = model_MovieUpDate.overview
            mov['categories'] = model_MovieUpDate.categories
            mov['year'] = model_MovieUpDate.year
            mov['rating'] = model_MovieUpDate.rating
            mov['poster_path']    = model_MovieUpDate.poster_path
    return JSONResponse(content=data_movies)

@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int)-> List[Movie_model]:
    for movie in data_movies:
        if movie['id'] == id:
            data_movies.remove(movie)
    return JSONResponse(content=data_movies)