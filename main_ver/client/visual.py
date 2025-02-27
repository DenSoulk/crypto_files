import json
from tkinter import *
import tkinter
from tkinter import ttk
import requests
import asyncio

class PlaceholderEntry(Entry):
    def __init__(self, master=None, placeholder="Введите текст", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self.get() == self.placeholder:
            self.delete(0, 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

async def send_message():# bladckai vesh по идеи должно быть асихронно
    message = entry.get()
    if message and message != entry.placeholder:
        response = requests.post('http://localhost:5000/test', json={"text": message})
        if response.status_code == 200:
            chat_box.config(state=NORMAL)
            chat_box.insert(END, f"Вы: {message}\n")
            chat_box.config(state=DISABLED)
            entry.delete(0, END)
            entry.put_placeholder()
        else:
            print("Error: Unable to send message")

async def get_chat_history(chat_id):#  на перепись всё. И что за бред? Почему мы вызываем получение чата, а по итогу у нас происходит ещё и его изменение В ФУНКЦИИ КОТОРАЯ ДОЛЖНА ПОЛУЧАТЬ СООБЩЕНИЯ  ?????
    response = requests.get(f'http://localhost:5000/test/{chat_id}')#переписать, не надо оно нам
    if response.status_code == 200:
        chat_data = response.json()
        update_chat_box(chat_data)
    else:
        print("Error: Unable to fetch chat history")

async def update_chat_box(chat_data):
    chat_box.config(state=NORMAL)
    chat_box.delete(1.0, END)
    for message in chat_data["messages"]:
        chat_box.insert(END, f"{message['user']}: {message['text']}\n")
    chat_box.config(state=DISABLED)


#это боковая шляпа
async def fetch_chat_partners():#явно не надо, переписать
    response = requests.get('http://localhost:5000/test')
    if response.status_code == 200:
        chat_data = response.json()
        display_chat_partners(chat_data)
    else:
        print("Error: Unable to fetch chat partners")

async def display_chat_partners(chat_data):
    for chat in chat_data["chats"]:
        inside_frame = Frame(frame)
        inside_frame.pack(fill=X, pady=5)

        user = Label(inside_frame, text=chat["name"])
        user.pack(side=LEFT, anchor=W, padx=5)

        open_button = Button(inside_frame, text="перейти", command=lambda chat_id=chat["ID"]: get_chat_history(chat_id))
        open_button.pack(side=RIGHT, padx=5)

root = Tk()
root.title("Your chat")

try:
    frame = Frame(root, bg="white", width=5)
    frame.pack(side=LEFT, anchor=NW, padx=0, pady=0, fill=BOTH, expand=True)

    fetch_chat_partners()

    send_button = Button(root, text="Отправить", command=send_message, cursor="hand2")
    send_button.pack(side=RIGHT, anchor=SE, fill=X, padx=5, pady=5)

    entry = PlaceholderEntry(root, placeholder="Введите текст")
    entry.pack(side=BOTTOM, fill=X, padx=5, pady=5)

    chat_box = Text(root, cursor="hand2")
    chat_box.config(state=DISABLED)
    chat_box.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

except:
    frame = Frame(root, bg="white", width=5)
    frame.pack(side=LEFT, anchor=NW, padx=0, pady=0, fill=BOTH, expand=True)

    send_button = Button(root, text="чекни инет", cursor="hand2")
    send_button.pack(side=RIGHT, anchor=SE, fill=X, padx=5, pady=5)

    entry = PlaceholderEntry(root, placeholder="ИНЕТА НЕМА")
    entry.pack(side=BOTTOM, fill=X, padx=5, pady=5)

    chat_box = Text(root, cursor="hand2", bg ='red', font=('Arial', 40), height=10, width=50)
    chat_box.config(state=NORMAL)
    chat_box.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

    chat_box.insert(1.0, "CHECK YOUR INTERNET CONNECTION")
    chat_box.config(state=DISABLED)

root.mainloop()



#Всё что выше крайне сомнительная вещь, что-то надо потырить, но переписать надо точно



async def ping_server(client_id): #Должно быть зациклена
    client_id=0#test
    data_json = requests.get(f'http://127.0.0.1:5000/ping/'+client_id)
    #ТУт data_json должно разбиваться на 2 пакета: пользователи, сообщения
    #Обновление входящих сообщений
    #Обновление списка пользователей
    await asyncio.sleep(1.5)


async def authorization_server(client_id,client_password):
    #по сути делается 1 раз в начале, но есть проблемы с безопасностью явные(подменой покетов можно будет отправлять сообщения не от своего лица ) но хз
    client_id=0#test
    data_json = requests.get(f'http://127.0.0.1:5000/ping/'+client_id)
    #Тут функция должна будет подтаскивать сообщения(Причём новые и старые) и их выводить
    #Вызов ping_server()

