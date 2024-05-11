import json
from numpy import dot
from numpy.linalg import norm
from openAIapi import obtain_embedding
from similitud import similitud_cos

dirBD = "C:/Users/Link_/Desktop/LA_II/Proyecto/COELNETSSO/entornoVirtual/BD/bd_prototipo.json"

texto = input("Ingresa Cadena a Clasificar: ")

#Obtiene vector del texto
vecInput = obtain_embedding(texto)

#Carga de Json con Clasificacion de Ordenes
with open(dirBD, 'r') as archivo:
    datos = json.load(archivo)

similitudes = []

#imprimir similitudes promedio por categoria
for clave, valor in datos.items():
    i = 0
    sum = 0.0
    
    for elemento in valor:
        vecBD=obtain_embedding(elemento)
        sim=similitud_cos(vecInput,vecBD)
        sum=sum+sim
        i=i+1

    similitudes.append(sum/i)
    print(clave + ": "+str(round(sum/i,3)))
print()

max_similitud = similitudes.index(max(similitudes))

i=0
for clave, valor in datos.items():
    if i == max_similitud:
        print("El texto tiene mayor similitud semantica con la Categoría: "+ clave)
        break
    i=i+1