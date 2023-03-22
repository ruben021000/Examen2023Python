import csv

url = "C://cosas uni//3Tercero//ExamenPython//Examen2023Python//winequality.csv"

def read_data(fichero):
    with open(fichero, 'r') as file:
        dic_anidado = {}
        dic = {}
        contador = 0
        reader = csv.reader(file)
        for row in reader:
            if row != 0:

                dic["type"] = row[0]
                dic["fixed acidity"] = row[1]
                dic["volatile acidity"] = row[2]
                dic["citric acid"] = row[3]
                dic["residual sugar"] = row[4]
                dic["chlorides"] = row[5]
                dic["free sulfur dioxide"] = row[6]
                dic["total sulfur dioxide"] = row[7]
                dic["density"] = row[8]
                dic["pH"] = row[9]
                dic["sulphates"] = row[10]
                dic["alcohol"] = row[11]
                dic["quality"] = row[12]

                dic_anidado["dato "+str(contador)] = dic
                contador = contador+1
    return dic_anidado

#print(read_data(url))


def split(dic_anidado):
    dic_white = {}
    dic_red = {}

    dic_white = { dic for dic in dic_anidado if dic_anidado[dic]["type"] == "white"}
    dic_red = { dic for dic in dic_anidado if dic_anidado[dic]["type"] == "red"}
    return dic_white, dic_red

dics = split(read_data(url))

def reduce(dic_anidado,atributo):
    #lista = [dic for dic in dic_anidado if atributo in dic[]]
    lista = []
    for dic in dic_anidado:
        for key in dic:
            lista.append(key)
    return lista

print(reduce(dics,"alcohol"))