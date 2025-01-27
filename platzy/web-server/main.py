import store
# from fastapi import FastAPI
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return list(range(1,5))

@app.get('/contact', response_class=HTMLResponse)
def get_company_name():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """

def run():
    print("in run", get_list(), get_company_name())
    store.get_categories()



if __name__ == '__main__':
    run()