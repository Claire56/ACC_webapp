from fastapi import FastAPI , Body , Form, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID



app = FastAPI()

class Book(BaseModel):
    id:UUID
    title: str = Field(min_length=1)
    author:str = Field(min_length=1, max_length = 100)
    rating : int = Field(gt=1, lt = 101)
    description: str = Field(min_length=1, max_length =200, title = "Description of the book")
    # class Config:
    #     schema_extra = {
    #         'examples':{
    #             id:'34fb0323-82bb-493c-b6c4-55af47f056b5',
    #             'title':'Lovely book',
    #             'rating':10,
    #             'description': 'Lovely book'
            
    #         }
    #     }
Books =[]

@app.get("/")
async def get_all_books():
    return Books

@app.post("/")
async def create_book(book:Book):
    Books.append(book)
    return Books

@app.put("/books/{book_UUID}")
async def update_book(book_uuid:str):
    
    return Books

@app.post("/books/{book_UUID}")
async def delete_book(book:Book):
    Books.append(book)
    return Books

@app.get("/books/login")
async def login(username: str = Form(), password: str = Form()):
    
    return {"username": username}