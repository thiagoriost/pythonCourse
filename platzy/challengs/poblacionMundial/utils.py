def get_population(countri_dictionario: str):
    """ keys = ['col', 'bol']
    values = [300, 400]
    populatio_dic = {
        '2022': int(countri_dictionario['2022 Population']),
        '2020': int(countri_dictionario['2020 Population']),
        '2015': int(countri_dictionario['2015 Population']),
        '2010': int(countri_dictionario['2010 Population']),
        '2000': int(countri_dictionario['2000 Population']),
        '1990': int(countri_dictionario['1990 Population']),
        '1980': int(countri_dictionario['1980 Population']),
        '1970': int(countri_dictionario['1970 Population']),
    } """
    
    labels = countri_dictionario.keys()
    values = countri_dictionario.values()    
    return labels, values

def population_by_country(data, country):
    
    # Crear un diccionario para almacenar población por año
    population_by_year = {}

    # Recorrer cada entrada en los datos
    for country_data in data:
        for key, value in country_data.items():
            if "Population" in key and key.split()[0].isdigit():
                year = key.split()[0]  # Extraer el año
                population = int(value)  # Convertir a entero
                if year not in population_by_year:
                    population_by_year[year] = 0
                population_by_year[year] += population  # Sumar la población al año correspondiente

    # Ordenar el diccionario por año (opcional, para presentación)
    population_by_year = dict(sorted(population_by_year.items()))

    # Imprimir el resultado
    print("population_by_year => ",population_by_year)
    return population_by_year
    # result = list(filter(lambda item: item['Country/Territory'] == country, data))
    # return result