# correr proyecto FastAPI
fastapi dev main.py
fastapi dev app/main.py

# cambiar puerto por defecto
desde cmd en la ubicacion del main.py ejecutar el siguiente comando, 5000 seria el puerto deseado
uvicorn main:app --port 5000

# hostiar la app para visualizar la api dedes el movil u otro pc pero en la misma red
uvicorn main:app --host 0.0.0.0 --port 5000 --reload


# revisar DB sqlite3
sqlite3 [nombre archivo db]
sqlite3 db.sqlite3
## ver tablas
    .tables

    .schema [nombreTabla]
    .schema customerplan

select * from [nombreTabla];

https://github.com/fastapi/full-stack-fastapi-template?tab=readme-ov-file

# revisar documentacion
## opcion 1
http://127.0.0.1:8000/docs

## opcion 2
http://127.0.0.1:8000/redoc