from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def root():
    return {"Message": "Hello FastAPI + RapidAPI Client!"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"Message": f"Hello, {name}!"}