from fastapi import FastAPI,HTTPException
from models import User
from pydantic import BaseModel

app = FastAPI()

users = [
        {
        'id' : 101,
        'name' : 'Ramesh',
        'email' : 'ramesh@email.com',
        'age' : 24
        },
        {
        'id' : 102,
        'name' : 'Kavya',
        'email' : 'kavya@email.com',
        'age' : 22
        },
        {
        'id' : 103,
        'name' : 'Pawan',
        'email' : 'pawan@email.com',
        'age' : 25
        }
]

@app.post("/post_user")
async def register_user(user: User):
    for existing_user in users:
        if existing_user['id'] == user.id:
            raise HTTPException(
        status_code = 404,
        detail = f"user with {user.id} already exist!" )

    users.append(user.model_dump())
    return {'message': 'user added succesfully', "user": user}

@app.put('/update/{user_id}')
async def fetch_user(updated_user: User, user_id: int):
    for user in users:
        if user['id'] == user_id:
            user.update(updated_user.model_dump())
            return ({'message': "User updated succefully!"}, {'user':user})
            
    raise HTTPException(
        status_code= 404,
        detail = f"user with user id {user_id} does not exist!" )

@app.get("/users/{user_id}")
async def fetch_users(user_id: int):
    for user in users:
        if user['id'] == user_id:
            return user
    raise HTTPException(
        status_code = 404,
        detail = f"user with {user_id} does not exist!"
    )
        


@app.delete("/delete_users/{user_id}")
async def delete_user(user_id: int):
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(
        status_code = 404,
        detail = f"user with user id {user_id} does not exist!" 
    )

