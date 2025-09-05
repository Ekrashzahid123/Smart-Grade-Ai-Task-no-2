from fastapi import FastAPI,Query
from fastapi.responses import JSONResponse
import json

app = FastAPI()

def load_data():
    with open('student.json','r') as f:
     data=json.load(f)
    return data 

@app.get('/view')
def view():
   data=load_data()
   if not data:
      return JSONResponse(status_code=404,content={"Error,No student founf"})
   return data 

@app.get("/student/{student_id}")
def get_student(student_id: str):
    data = load_data()
    for student in data.get("students", []): 
        if student["id"] == student_id:
            return student
    return JSONResponse(status_code=404,content={"error": f"Student with id {student_id} not found"}
    )
@app.get("/studentsorting")
def get_students(order: str = Query("asc", enum=["asc", "desc"])):
    data = load_data()
    students = data.get("students", [])

    if not students:
        return JSONResponse(status_code=404, content={"error": "No student data found"})
    return {
        "students": sorted(students, key=lambda x: x["cgpa"], reverse=(order == "desc"))
    }

   
         
