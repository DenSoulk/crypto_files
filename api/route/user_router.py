from fastapi import APIRouter, HTTPException
from api.sqlite_conf import user_session as session
from api.models.user import User
from sqlalchemy import text

router = APIRouter()

@router.get("/user")
def get_user():
    users = session.execute(text("SELECT * FROM user"))
    return [dict(user._mapping) for user in users]

@router.post("/user")
async def create_user(name: str, login: str, password: str):
    user = User(name=name, login=login, password=password)
    session.add(user)
    session.commit()
    return{"message": "User created"}
    
@router.delete("/user/{id}")
async def delete_user(id: int):
    user = session.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return{"message": "User deleted"}
    
@router.put("/user/{id}")
async def update_user(id: int, name: str, login: str, password: str):
    user = session.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = name
    user.login = login
    user.password = password
    session.commit()
    return{"message": "User updated"}