import requests
import httpx
#from starlette.responses import StreamingResponse


def callService(body: dict):
    url = "http://localhost:11434/api/chat"
    try:

        with httpx.Client(timeout=300) as client:
            #return StreamingResponse(client.post(url,json=body).json())
            res=client.post(url,json=body)
            return res.json()
    except:
        return None
    # res = requests.post(
    #     "http://api.com/users/123",  # path param goes in the URL directly
    #     params={"page": 1},  # query params
    #     headers={"Authorization": "Bearer token"},  # headers
    #     json={"name": "John"}  # request body
    # ).json()
    # print(res.json())
def callEmbeddingService(body:dict):
    url="http://localhost:11434/api/embeddings"
    try:
        with httpx.Client(timeout=300) as client:
            res=client.post(url,json=body)
            return res.json()
    except:
        return None