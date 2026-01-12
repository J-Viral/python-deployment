from fastapi import FastAPI

app = FastAPI(title="Hello World API")

@app.get("/")
def root():
    return {"message": "Hello World"}


#http://127.0.0.1:8000/