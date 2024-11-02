import json
from openAIapi import obtain_embedding
from similitud import similitud_cos

def compareText(text):
    dirBD = "C:/Proyectos/COELNETSSO/BD/data_with_embeddings.json"

    with open(dirBD, 'r') as archivo:
        data = json.load(archivo)
    
    similitudes = []

    embedding_texto=obtain_embedding(text)

    # Imprimir similitudes promedio por categoría
    for clave, valor in data.items():
        sum_similitud = 0.0
        contador = 0

        for elemento in valor:
            vecBD = elemento["embedding"]
            sim = similitud_cos(embedding_texto, vecBD)
            sum_similitud += sim
            contador += 1

        similitud_promedio = sum_similitud / contador if contador > 0 else 0
        similitudes.append(similitud_promedio)
        print(f"{clave}: {round(similitud_promedio, 3)}")

    # Identificar la categoría con mayor similitud
    max_similitud = max(similitudes)
    categoria_max_similitud = list(data.keys())[similitudes.index(max_similitud)]

    print("\nEl texto tiene mayor similitud semántica con la Categoría:", categoria_max_similitud)
    return similitudes

if __name__ == "__main__":
    compareText('como mis como')