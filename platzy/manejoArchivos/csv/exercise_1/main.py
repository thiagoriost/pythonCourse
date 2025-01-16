import os, csv

path = os.getcwd()+r"\platzy\manejoArchivos\csv\exercise_1\data.scv"

def read_csv(path):
    with open(path, 'r') as csvFile:
        fileReaded = csv.reader(csvFile, delimiter=',')
        """  reader = list(fileReaded)
        data = []
        for row in reader:
            data.append(row[1])
        total = 0
        for e in data:
            total += int(e) """
        return sum(int(row[1]) for row in fileReaded)

response = read_csv(path)
print(response)