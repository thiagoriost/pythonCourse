import os, csv
import utils
import chart, world_population_analitic



path = os.getcwd()+r"\platzy\manejoArchivos\csv\world_population.csv"

def run():
    data = world_population_analitic.read_csv(path)
    country = input("Ingrese pais: ")
    
    result = utils.population_by_country(data, country) 
    
    if len(result) > 0: 
        # country = result[0]
        print("result => ", result)
        keys, values = utils.get_population(result)
        print("keys, values => ", keys, values)
        chart.generate_bar_char(keys, values)
        return




if __name__ == '__main__':
    run()
    
"""     
aa = [
    {'Rank': '36', 'CCA3': 'AFG', 'Country/Territory': 'Afghanistan', 'Capital': 'Kabul', 'Continent': 'Asia', '2022 Population': '41128771', '2020 Population': '38972230', '2015 Population': '33753499', '2010 Population': '28189672', '2000 Population': '19542982', '1990 Population': '10694796', '1980 Population': '12486631', '1970 Population': '10752971', 'Area (kmÂ²)': '652230', 'Density (per kmÂ²)': '63.0587', 'Growth Rate': '1.0257', 'World Population Percentage': '0.52'},
    {'Rank': '138', 'CCA3': 'ALB', 'Country/Territory': 'Albania', 'Capital': 'Tirana', 'Continent': 'Europe', '2022 Population': '2842321', '2020 Population': '2866849', '2015 Population': '2882481', '2010 Population': '2913399', '2000 Population': '3182021', '1990 Population': '3295066', '1980 Population': '2941651', '1970 Population': '2324731', 'Area (kmÂ²)': '28748', 'Density (per kmÂ²)': '98.8702', 'Growth Rate': '0.9957', 'World Population Percentage': '0.04'},
    {'Rank': '34', 'CCA3': 'DZA', 'Country/Territory': 'Algeria', 'Capital': 'Algiers', 'Continent': 'Africa', '2022 Population': '44903225', '2020 Population': '43451666', '2015 Population': '39543154', '2010 Population': '35856344', '2000 Population': '30774621', '1990 Population': '25518074', '1980 Population': '18739378', '1970 Population': '13795915', 'Area (kmÂ²)': '2381741', 'Density (per kmÂ²)': '18.8531', 'Growth Rate': '1.0164', 'World Population Percentage': '0.56'}
    ] """