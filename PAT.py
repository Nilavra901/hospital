from fastapi import FastAPI

app=FastAPI()
@app.get("/")
def about():
    return {"message":'Hello, World! This is a FastAPI application.'}

