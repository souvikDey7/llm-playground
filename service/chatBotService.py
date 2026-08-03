from streamlit import empty

from modelClientConnector import ollamaClient
from service import ragRepoService

"""
{
  "model": "claude-sonnet-4-6",
  "messages": [
    {"role": "user", "content": "hi"},
    {"role": "assistant", "content": "hello!"},
    {"role": "user", "content": "what is python?"},
    {"role": "assistant", "content": "Python is..."},
    {"role": "user", "content": "give me an example"}
  ]
}
"""
msgDB=[]
def chatService(message:str):
    while len(msgDB)>10:
        msgDB.pop(0)

    embd=creatingEmbedding(message)
    vectors=getVectorContext(embd)

    user={"role":"user","content":"Context:"+vectors+"\nQuestion"+message}
    print(user)

    msgDB.append(user)

    body={
        "model":"llama2",
        "messages":msgDB,
        "stream" : False
    }
    body=ollamaClient.callService(body)
    #print(body)
    if body and body.get("message"):
        model = {"role": "assistant", "content": body.get("message").get("content")}
        msgDB.append(model)
        return body.get("message").get("content")
    msgDB.pop()
    return "service is down"

def creatingEmbedding(text:str):
    return ragRepoService.callEmbeddingService(text,False)

def getVectorContext(vector:list):
    vectors=ragRepoService.getVectorContext(vector)
    return "\n".join(vectors)