from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {'message': 'Connected'}

@app.get("/hello")
def hello():
    return {'message': 'Hello World'}
