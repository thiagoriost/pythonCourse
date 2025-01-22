import matplotlib.pyplot as plt
import pandas
import os


def pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()
    
    

path = os.getcwd()+r"\world_population.csv"
print(path)
dataFrame = pandas.read_csv(path)

dataFrame = dataFrame[dataFrame['Continent'] == 'South America']
countries = dataFrame['Country/Territory'].values
print("countries => ", countries)
percentages = dataFrame['World Population Percentage'].values
print("percentages => ", percentages)
pie_chart(countries, percentages)
