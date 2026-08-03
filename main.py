
from fastapi import FastAPI
from controller import ChatController

app=FastAPI()
app.include_router(ChatController.rt)

@app.get("/check")
def check():
    return "server in up"