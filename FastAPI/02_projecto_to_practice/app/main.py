from typing import List
from fastapi import Body, FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse
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

def get_movie_by_id(data_movies, movie_id)-> Movie_model:

    for movie in data_movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found") 

def get_movie_by_category_and_year(data_movies, category:str, year:int)-> Movie_model:
    category = category.lower()
    for movie in data_movies:
        if category in [cat.lower() for cat in movie["categories"]] and movie["year"] == year:
            return movie
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found") 

@app.get("/", tags=["Home"])
def home():
    return HTMLResponse(content="<h1>Welcome to my first FastAPI project</h1>", status_code=200)

@app.get("/movies", tags=["movies"])
def movies() -> List[Movie_model]:
    # return {"Hello": "World!!!!"}
    return data_movies

@app.get("/movies/{id}", tags=["movies"])
def moviesByID(id: int)-> Movie_model:
    movie = get_movie_by_id(data_movies, id)
    return movie

@app.get("/movies/", tags=["movies"])
def moviesByCategory(category: str, year:int)-> Movie_model:
    movie = get_movie_by_category_and_year(data_movies, category, year)
    return movie

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
    return data_movies

@app.post("/movies2", tags=['movies'])
def create_movie_from_model(movie_model: Model_Movie_Create) -> List[Movie_model]:
    print("movie_model => ", movie_model)
    data_movies.append(movie_model.model_dump())
    return data_movies

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
    return data_movies

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
    return data_movies

@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int)-> List[Movie_model]:
    for movie in data_movies:
        if movie['id'] == id:
            data_movies.remove(movie)
    return data_movies