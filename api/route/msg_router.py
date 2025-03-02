from fastapi import APIRouter, HTTPException
from api.sqlite_conf import msg_session as session
from api.models.msg import Message
from sqlalchemy import text

router = APIRouter()

@router.get("/msg")
def get_all_msg():
    users = session.execute(text("SELECT * FROM message"))
    return [dict(user._mapping) for user in users]



@router.post("/msg_onidsender/{id_sender}")
def get_all_msg(id_sender: int):
    users = session.execute(text(f'SELECT * FROM message WHERE id_sender={id_sender}'))
    return [dict(user._mapping) for user in users]

@router.post("/msg")
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
