from fastapi import APIRouter
newsRouter= APIRouter()
import subprocess


@newsRouter.get("/scrape")
def get_course():
    
   subprocess.Popen(["python3","news/news_scrape.py"])

   return {"message":"scrapping started"}

   