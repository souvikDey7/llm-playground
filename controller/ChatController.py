from fastapi import APIRouter
from model import ChatModel
from service import chatBotService, ragRepoService

rt=APIRouter()

@rt.post("/chat")
def chatBot(messageModel:ChatModel.ChatModel):
    return chatBotService.chatService(messageModel.message)
    #return "bot is down at this momment :"+messageModel  .message

@rt.post("/embedding")
def createEmbedding(messageModel:ChatModel.ChatModel):
    return ragRepoService.callEmbeddingService(messageModel.message,True)