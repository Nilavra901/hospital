from fastapi import FastAPI,Path,HTTPException,Query

app=FastAPI()
def load_data(patient_id:str=Path(...,description="The ID of the patient to retrieve")):
    with open ("data.txt", "r") as file:
        data = json.load()
@app.get("/")
def about():
    return {"message":'Hello, World! This is a FastAPI application.'}
 @app.get("/view-data")
 def view_data():
     data = load_data()
    return data
@app.get("?patient/{patient_id}")
def view_patient(patient_id: int):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail ="Patient not found")
@app.get('/sort')
def sort_patients(sort_by: str=Query(...,description='sort on the basis of height ,weight'))
    
    