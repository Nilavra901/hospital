from fastapi import FastAPI

app=FastAPI()
def load_data():
    with open ("data.txt", "r") as file:
        data = json.load()
@app.get("/")
def about():
    return {"message":'Hello, World! This is a FastAPI application.'}
 @app.get("/view-data")
    def view_data():
        data = load_data()
        return data
    