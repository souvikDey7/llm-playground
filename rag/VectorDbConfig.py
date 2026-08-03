import json

import chromadb
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("my_collection")

"""
collection.add(
    ids=["chunk_1"],
    embeddings=[[0.23, 0.45, ...]],
    documents=["FastAPI is a Python web framework"]
)"""

def addIntoDB(ids:str,emb:list,doc:str):
    collection.add(ids=[ids],embeddings=[emb],documents=[doc])
    print(collection.peek())

def getVectortToken(vector:list):
    return collection.query(query_embeddings=[vector], n_results=2)
