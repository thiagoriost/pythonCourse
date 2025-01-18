import os, csv

path = os.getcwd()+r"\platzy\manejoArchivos\csv\world_population.csv"
# E:\software\PYTHON\platzy\manejoArchivos\csv\world_population.csv

def read_csv(path):
    with open(path, 'r') as csvFile:
        fileReaded = csv.reader(csvFile, delimiter=',')
        header = next(fileReaded)
        reader = list(fileReaded)
        # print("header => ", header)
        data = []
        for row in reader:
            # print('*'*20)
            # iterable = list(zip(header, row))
            iterable = zip(header, row)
            # print(iterable)
            country_dictionari = {key: value for key, value in iterable}
            # print(country_dictionari)
            data.append(country_dictionari)
        # print('*'*20)
        # print("data => ", data)
        # print('*'*20)
        # print("data[0] => ", data[0])
        return data


if __name__ == '__main__':    
    read_csv(path)
else:
    print("__name__ => ", __name__)