from flask import Flask
from flask import jsonify
import asyncio
import requests
name="main"
app = Flask(name)
"""
@app.route('/message/<id>+<text>')
async def message(id,text):
"""

@app.route('/ping/<id>')
async def ping(id):
    request_messages = requests.get(f"http://0.0.0.0:8000/msg_to_user/{id}").json()

    #0.0.0.0:8000/msg?id_sender=1&id_reciever=1&text=zov&attachment=&is_sent=0&is_read=0
    #Подтягиваем Данные из базы и также ждём где-то 3 секунды и берём всех пользователей которые кинули пинг
    # кидаем пользоваетелям
    return jsonify()

@app.route('/mess/<id_sender>+<id_reciever>+<message>+<attachment>')
async def mess(id_sender,id_reciever,message,attachment):
    request_messages = requests.post(f"http://127.0.0.1:8000/msg/?id_sender={id_sender}&id_reciever={id_reciever}&text={message}&attachment={attachment}&is_sent=1&is_read=0")
    return jsonify()

@app.route('/authorization/<id>')
async def authorization(id):# Какие строчки закидывать это надо по базе смотреть
    #Подтягивем чаты
    return jsonify()


if __name__ == '__main__':
    app.run()