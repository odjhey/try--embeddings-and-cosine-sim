import sqlite3
import pickle

database_name = 'somedatabase.db'

# Connect to SQLite database (it will create one if it doesn't exist)
conn = sqlite3.connect(database_name)
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE IF NOT EXISTS poems
             (id INTEGER PRIMARY KEY, text TEXT, embedding BLOB)''')

# Function to insert a poem and its embedding
def insert_poem(text, embedding):
    embedding_blob = pickle.dumps(embedding)
    c.execute('INSERT INTO poems (text, embedding) VALUES (?, ?)', (text, embedding_blob))
    conn.commit()


def fetch_embedding(poem_id):
    # Connect to SQLite database (it will create one if it doesn't exist)
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute('SELECT embedding FROM poems WHERE id = ?', (poem_id,))
    embedding_blob = c.fetchone()[0]
    embedding = pickle.loads(embedding_blob)
    conn.close()
    return embedding