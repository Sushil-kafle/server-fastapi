from fastapi import FastAPI
from routes.news import newsRouter
from decouple import config
import uvicorn
import os

CLIENT_URL = os.getenv("CLIENT_URL",config("CLIENT_URL"))



from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(newsRouter, prefix="/news")

PORT = os.getenv("PORT",8000)


if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=PORT, reload=True)
    server = uvicorn.Server(config)
    server.run()
