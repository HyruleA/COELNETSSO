import os
from openai import OpenAI
api_keyVal = os.getenv('OPENAI_API_KEY')

client = OpenAI(
   api_key= api_keyVal,
)

frase1 ="Abrir la puerta automatica"
frase2 = "Permitir entrar a la cochera"
orden = "Abrir la cochera"

responseO = client.embeddings.create(
    input = orden,
    model="text-embedding-3-small"
)
vectorO = responseO.data[0].embedding


response1 = client.embeddings.create(
    input = frase1,
    model="text-embedding-3-small"
)
vector1 = response1.data[0].embedding

response2 = client.embeddings.create(
    input=frase2,
    model="text-embedding-3-small"
)
vector2 = response2.data[0].embedding

print(frase1,":",vector1[:10])
print(frase2,":",vector2[:10])
print(orden,":",vectorO[:10])