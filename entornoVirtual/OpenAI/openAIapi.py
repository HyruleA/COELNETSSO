import os
from openai import OpenAI

api_keyVal = os.getenv('OPENAI_API_KEY')

client = OpenAI(
   api_key= api_keyVal,
)

def obtain_embedding(texto):
    embedding = client.embeddings.create(
        input = texto,
        model="text-embedding-3-small"
    )
    embe_vector = embedding.data[0].embedding
    return embe_vector