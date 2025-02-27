from fastapi import APIRouter, HTTPException
from api.sqlite_conf import msg_session as session
from api.models.msg import Message
from sqlalchemy import text
router = APIRouter()



@router.get("/msg_form_id_to_id_user/{id_sender}&{id_reciever}")
def msg_form_id_to_id_user(id_sender: int,id_reciever):
    users = session.execute(text(f"SELECT * FROM message WHERE id_sender = {id_sender} AND id_reciever={id_reciever} AND is_read = {0}"))
    return [dict(user._mapping) for user in users]

@router.get("/chats_to_user/{id}")
def chats_to_user(id: int):
    users_id = session.execute(text(f"SELECT DISTINCT id_sender FROM message WHERE id_reciever = {id}"))#тут получаю уникальные айдишники
    #тут надо для всех айдишников имена найти
    #и отпрваить надо айди и имена пользователей
    return [dict(user._mapping) for user in users]











@router.post("/msg/")
def create_msg(id_sender: int, id_reciever: int, text: str, attachment: str, is_sent: bool, is_read:bool):
    msg = Message(id_sender=id_sender, id_reciever=id_reciever, text=text,attachment=attachment, is_sent=is_sent, is_read=is_read)
    session.add(msg)
    session.commit()
    return{"message": "Message created"}

@router.delete("/msg/{id}")
def delete_msg(id: int):
    msg = session.query(Message).filter(Message.id == id).first()
    if not msg:
        raise HTTPException(status_code=404, detail="Message not found")
    session.delete(msg)
    session.commit()
    return{"message": "Message deleted"}

@router.put("/msg/{id}")
def update_msg(id: int, id_sender: int, id_reciever: int, text: str, attachment: str, is_sent: bool, is_read:bool):
    msg = session.query(Message).filter(Message.id == id).first()
    if not msg:
        raise HTTPException(status_code=404, detail="Message not found")
    msg.id_sender = id_sender
    msg.id_reciever = id_reciever
    msg.text = text
    msg.attachment = attachment
    msg.is_sent = is_sent
    msg.is_read = is_read
    session.commit()
    return{"message": "Message updated"}

@router.get("/all_msg")
def get_all_msg():
    users = session.execute(text("SELECT * FROM message"))
    return [dict(user._mapping) for user in users]