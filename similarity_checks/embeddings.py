import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')
client = openai.OpenAI()

def get_embeddings(text):
    response = client.embeddings.create(
        input=[text],
        model="text-embedding-3-small"
    )
    embedding = response.data[0].embedding
    return embedding
