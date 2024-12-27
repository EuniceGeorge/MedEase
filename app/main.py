#create a FastApi App
from fastapi import FastAPI, Path
from pydantic import BaseModel


app= FastAPI()


@app.get("/")
async def root():
     return {"message": "Hello world now!!"}

@app.get("/create")
async def create():
     return {"data": "hello people"}

@app.post("/createpost")
async def reqpost():
    return {"message": "successfully sent"}

@app.get("/hello/{name}")
async def tut(name:str=Path(...,min_length=3, max_length=10)):
    return {"name":name}
