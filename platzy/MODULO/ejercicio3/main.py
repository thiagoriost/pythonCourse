import utils

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

def run():
    key, values = utils.get_population()
    print("key, values => ", key, values)

    country = input("Type Country => ")

    result = utils.population_by_country(data, country)
    print("result => ", result)

if __name__ == '__main__':
    run()