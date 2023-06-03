from datetime import date, datetime, timedelta
from typing import Union
from model import User
import auth, model
from pydantic import BaseModel

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(auth.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to the specific origins you want to allow
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestBody(BaseModel):
    username: str
    password: Union[str, None] = None
    birthday: Union[date, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/user/", response_model=User)
def read_users_me(
    current_user: User = Depends(auth.get_current_active_user)
):
    current_user.password = ""
    return current_user

@app.post("/user/")
def create_user(
    request_body: RequestBody
):
    username = request_body.username
    password = request_body.password
    birthday = request_body.birthday
    result = model.create_user(username, auth.get_password_hash(password), birthday)
    if result == False:
        raise HTTPException(
            status_code=409,
            detail="Username already exist.",
        )
    return {"result": result}

@app.put("/user/")
def update_user(
    request_body: RequestBody,
    current_user: User = Depends(auth.get_current_active_user)
):
    username = request_body.username
    password = request_body.password
    birthday = request_body.birthday
    if current_user.username != username:
        raise HTTPException(
            status_code=403,
            detail="You can't modify other user's information.",
        )
    if password:
        result = model.update_user(username, auth.get_password_hash(password), birthday)
    else:
        result = model.update_user(username, None, birthday)
    return {"result": result}

@app.delete("/user/")
def delete_user(
    request_body: RequestBody,
    current_user: User = Depends(auth.get_current_active_user)
):
    
    print('deleting...')
    username = request_body.username
    if current_user.username != username:
        raise HTTPException(
            status_code=403,
            detail="You can't delete other user.",
        )
    result = model.delete_user(username)
    return {"result": result}
