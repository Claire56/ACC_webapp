from fastapi import FastAPI , Depends , HTTPException 
from db import engine , SessionLocal
import models 
from sqlalchemy.orm import session
from pydantic import BaseModel , Field 
from typing import Optional


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class Todo(BaseModel):
    title : str 
    description: Optional[str]
    priority  : int = Field(gt=0, lt=6)
    complete : bool
     

@app.get("/")
async def read_all(db:session = Depends(get_db) ):
    return db.query(models.Todos).all()

@app.get("/todo/{todo_id}")
async def read_todo(todo_id: int , db:session = Depends(get_db) ):
    result = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    if result is not None:
        return result
    else:
        raise http_Exception()
    
@app.post("/")
async def create_todo(todo: Todo , db:session = Depends(get_db)):
    todo_model = models.Todos()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete
    
    db.add(todo_model)
    db.commit()
    return {
        'status': 201, 'transaction': "Successful"
    }


@app.put("/todo/{todo_id}")
async def update_todo(todo_id: int , todo: Todo , db:session = Depends(get_db) ):
    result = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    if result is  None:
        raise http_Exception()
    else:
        result.title = todo.title
        result.description = todo.description
        result.priority = todo.priority
        result.complete = todo.complete

        db.add(result)
        db.commit()
        return {
            'status': 200, 'transaction': "Successful"
        }


        
    
@app.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int , todo: Todo , db:session = Depends(get_db) ):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    if todo_model is None:
        raise http_Exception()
    db.query(models.Todos).filter(models.Todos.id == todo_id).first().delete()
    
    db.commit()
    return {
            'status': 200, 'transaction': "Successful"
        }
    
    
def http_Exception():
        return  HTTPException(status_code= 404, detail='Todo not found ')