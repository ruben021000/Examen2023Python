import csv

url = "C://cosas uni//3Tercero//ExamenPython//Examen2023Python//winequality.csv"

def read_data(fichero):
    with open(fichero, 'r') as file:
        dic = {}
        contador = 0
        contador_lineas = 0
        reader = csv.reader(file)
        for row in reader:
                dic = {row[0]:row} 
    return dic

print(read_data(url))


def split(dic):
    dic_white = {}
    dic_red = {}

    for key in dic:
       # if dic[key]["white"]:
        #    dic_white.append(dic[key])
        print(dic[key])
    return dic_white, dic_red



dic = {"dato1":{
    "type":"white",
    "fixed acidity":"7",
    "volatile acidity":"0,27",
    "citrid acid":"0.36"
},"dato2":{
    "type":"white",
    "fixed acidity":"7",
    "volatile acidity":"0,27",
    "citrid acid":"0.36"}

}

