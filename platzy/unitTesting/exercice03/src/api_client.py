import requests

def get_location(ip):
    url = f"http://freeipapi.com/api/json/{ip}"
    response = requests.get(url)
    response.raise_for_status() # controla exepcion
    data = response.json()
    # import ipdb; ipdb.set_trace()
    return {
        "country": data["countryName"],
        "region": data["regionName"],
        "city": data["cityName"],
    }
    
if __name__ == "__main__":
    ipGoogle = "8.8.8.8"
    response = get_location(ipGoogle) 
    print(response)