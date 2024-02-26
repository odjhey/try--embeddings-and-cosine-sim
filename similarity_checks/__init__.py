__version__ = '0.1.0'

from .db import insert_poem, fetch_embedding
from .embeddings import get_embeddings 
from .similarity import calculate_similarity

def main():
  # insert_poem('asnother entry', 'ohoooh')
  text = 'pako 3 inches'
  embed = get_embeddings(text)
  insert_poem(text, embed)

def select():
  # res = fetch_embedding(7)
  # print('result')
  # print(res)

  ids = [7, 8, 9, 10, 11]
  similarities = []
  # Calculate similarity between each pair of embeddings
  for i in range(len(ids)):
    for j in range(i + 1, len(ids)):  # Ensure each pair is only compared once
      emb1 = fetch_embedding(ids[i])
      emb2 = fetch_embedding(ids[j])
      
      similarity = calculate_similarity(emb1, emb2)
      similarities.append(((ids[i], ids[j]), similarity))

  for pair, similarity in similarities:
    print(f"Similarity between {pair[0]} and {pair[1]}: {similarity}")

  # # Calculate similarity between the first two poems in the database
  # em1 = fetch_embedding(7)
  # em2 = fetch_embedding(10)
  # similarity = calculate_similarity(em1, em2)
  # print(f"Similarity: {similarity}")
