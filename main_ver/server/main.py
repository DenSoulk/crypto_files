import sqlite3
import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from api.route.msg_router import router as msg_router
from api.route.user_router import router as user_router

# Подключаемся к базе данных
conn = sqlite3.connect('user.db')
c = conn.cursor()
app = FastAPI()

app.include_router(msg_router)
app.include_router(user_router)


# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)