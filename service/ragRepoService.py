
from modelClientConnector import ollamaClient
from rag import VectorDbConfig
import uuid

def callEmbeddingService(text:str,indexStep:bool):
    dict={
        "model":"nomic-embed-text",
        "prompt":text
    }
    res=ollamaClient.callEmbeddingService(dict)
    if res and res.get("embedding"):
        if indexStep:
            createVectorArray(res.get("embedding"), text)
            return "data save"
        return res.get("embedding")
    return None

def createVectorArray(emb:list,text:str):
    id=uuid.uuid4().__str__() # I can use timestamp here also
    VectorDbConfig.addIntoDB(id,emb,text)

def getVectorContext(vector:list):
    res=VectorDbConfig.getVectortToken(vector)
    return res["documents"][0]