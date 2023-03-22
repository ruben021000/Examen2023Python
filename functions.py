import csv


def read_data(fichero):
    with open(fichero, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

print(read_data("winequality.csv"))


dic = {{"dato1":{
    "type":"white",
    "fixed acidity":"7",
    "volatile acidity":"0,27",
    "citrid acid":"0.36"
}}}