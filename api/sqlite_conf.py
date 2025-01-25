from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

user_engine = create_engine('sqlite:///user.db')
msg_engine = create_engine('sqlite:///message.db')

UserSession = sessionmaker(bind=user_engine)
user_session = UserSession()
MsgSession = sessionmaker(bind=msg_engine)
msg_session = MsgSession()
