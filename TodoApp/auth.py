from fastapi import FastAPI 
from pydantic import BaseModel
from typing import Optional
import models 


class CreateUser(BaseModel):
    username:str
    password : str
    email: str
    first_name : str
    last_name: str
    is_active : bool


app = FastAPI()


@app.post("/users/create_user")
async def create_user(new_user: CreateUser):
    user_model = models.Users()
    user_model.email =new_user.email
    user_model.fist_name = new_user.first_name
    user_model.hash_password = new_user.password
    user_model.is_active= new_user.is_active
    user_model.last_name = new_user.last_name

    return user_model

