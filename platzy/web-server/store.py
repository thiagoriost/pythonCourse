import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print("status_code => ", r.status_code)
    # print("text => ", r.text)
    # print("type => ", type(r.text))
    # pasar a formato json
    categories = r.json()
    # print("categories => ", categories)
    print("categories[0] => ", categories[0])
    print("categories[0] => ", categories[0].keys())
