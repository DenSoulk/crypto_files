import requests
#send_server=requests.get("http://127.0.0.1:5000/mess/1+1+test+ ")
#ping_request=requests.get("http://127.0.0.1:8000/msg_form_id_to_id_user/1&1")
#ping_request=requests.post("http://127.0.0.1:8000/msg/{id_sender}&{id_reciever}&{text}&{attachment}&{is_sent}&{is_read}")
#send_server=requests.post("http://127.0.0.1:8000/msg/?1+1+test+''+1&0")
#ping_request=requests.post("http://127.0.0.1:8000/msg/?id_sender=2&id_reciever=2&text=ruhu&attachment=rhffhu&is_sent=0&is_read=0")
get_chats=requests.get("http://127.0.0.1:8000/chats_to_user/1")
print(get_chats)