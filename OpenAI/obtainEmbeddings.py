import json
from numpy import dot
from numpy.linalg import norm
from openAIapi import obtain_embedding
from similitud import similitud_cos

def clasifica():
    dirBD = "C:/Proyectos/COELNETSSO/BD/datasetJson.json"

    with open(dirBD, 'r') as archivo:
        data = json.load(archivo)

    
    processed_data = {}
    for category, texts in data.items():
        processed_data[category] = []
        for text in texts:
            embedding = obtain_embedding(text)
            processed_data[category].append({
                "text": text,
                "embedding": embedding
            })
            
    
    with open("data_with_embeddings.json", "w", encoding="utf-8") as f:
        json.dump(processed_data, f, indent=4, ensure_ascii=False)

    print("Embeddings generados y guardados en data_with_embeddings.json")

if __name__ == "__main__":
    clasifica()