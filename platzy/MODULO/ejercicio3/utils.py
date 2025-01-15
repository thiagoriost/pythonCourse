def get_population():
    key = "Country"
    values = "4"
    return key, values

def population_by_country(data, country):
    response = list(filter(lambda e : e['Country'] == country, data))
    print("response => ", response)
    return response

data = [
        {
            'Country': 'Colombia',
            'Population': '500'
        },
        {
            'Country': 'Bolivia',
            'Population': '300'
        }
    ]
""" 
res = population_by_country(data, "Bolivia")
print("res => ", res)
 """