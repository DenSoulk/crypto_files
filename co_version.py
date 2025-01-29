import json
from tkinter import *
import tkinter
from tkinter import ttk
import requests

def send_message():
    message = entry.get()  # Получаем текст из поля ввода
    if message:
        # Отправляем сообщение на сервер
        response = requests.post('АРТЕМ СДЕЛАЙ', json={"text": message})
        if response.status_code == 200:
            chat_box.config(state=NORMAL)
            chat_box.insert(END, f"Вы: {message}\n")
            chat_box.config(state=DISABLED)
            entry.delete(0, END)  # Очищаем поле ввода
        else:
            print("Error: Unable to send message")

def update_chat_box(chat_data):
    chat_box.config(state=NORMAL)
    chat_box.delete(1.0, END)  # Очистка текущего текста
    for message in chat_data["messages"]:
        chat_box.insert(END, f"{message['user']}: {message['text']}\n")
    chat_box.config(state=DISABLED)

def get_chat_history(chat_id):
    response = requests.get(f'АРТЕМ СДЕЛАЙ/{chat_id}')  # Замените на свой URL
    if response.status_code == 200:
        chat_data = response.json()
        update_chat_box(chat_data)
    else:
        print("Error: Unable to fetch chat history")

def fetch_chat_partners():
    response = requests.get('АРТЕМ СДЕЛАЙ')  # Замените на свой URL
    if response.status_code == 200:
        chat_data = response.json()
        display_chat_partners(chat_data)
    else:
        print("Error: Unable to fetch chat partners")

def display_chat_partners(chat_data):
    for chat in chat_data["chats"]:
        inside_frame = Frame(frame)
        inside_frame.pack(fill=X, pady=5)

        user = Label(inside_frame, text=chat["name"])
        user.pack(side=LEFT, anchor=W, padx=5)

        open_button = Button(inside_frame, text="перейти", command=lambda chat_id=chat["ID"]: get_chat_history(chat_id))
        open_button.pack(side=RIGHT, padx=5)

root = Tk()
root.title("Your chat")

frame = Frame(root, bg="white", width=5)
frame.pack(side=LEFT, anchor=NW, padx=0, pady=0, fill=BOTH, expand=True)

# При первом запуске запрашиваем данные о пользователях
fetch_chat_partners()

send_button = Button(root, text="Отправить", command=send_message, cursor="hand2")
send_button.pack(side=RIGHT, anchor=SE, fill=X, padx=5, pady=5)

entry = Entry(root)
entry.pack(side=BOTTOM, fill=X, padx=5, pady=5)

chat_box = Text(root, cursor="hand2")
chat_box.config(state=DISABLED)
chat_box.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

root.mainloop()
