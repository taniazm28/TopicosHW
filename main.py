from fastapi import FastAPI
from os import environ as env 
app = FastAPI()

@app.get("/")
def index():
    return {"details": f"Hello, world Secret = {env['MY_VARIABLE']}"}