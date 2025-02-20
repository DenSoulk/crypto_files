from tkinter import *
from tkinter import ttk 


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

def button_cmnd():
    message = entry.get()
    if message != "Введите текст" and message !='':
        chat_box.config(state=NORMAL)
        chat_box.insert(END, f"Вы: {message}\n")
        chat_box.config(state=DISABLED)
        entry.delete(0, END)
    # отправка на сервер. текст из строки ввода == messege
    # как тебе это нужно упаковать думай сам.
    # зацикленность делать НЕ НАДО!!! Я сам сделаю автоматический пинг

def cmd_for_start():
    # спрашивает у сервера список чатов
    # мне нужно только чтобы результатом я имел "имя_переменной = file.json"
    


root = Tk()
root.minsize(width=600, height = 400)


frame = Frame(root, bg= "#c2ffea", width=170)
frame.pack(side=LEFT, anchor=NW, padx=0, pady=0, fill=BOTH, expand = False) 

send_button = Button(root, text="Отправить", command= button_cmnd, cursor="hand2")
send_button.pack(side=RIGHT, anchor=SE, fill=X, padx=5, pady=5)

entry = PlaceholderEntry(root, placeholder="Введите текст")  # Используем PlaceholderEntry
entry.pack(side=BOTTOM, fill=X, padx=5, pady=5)

chat_box = Text(root, cursor="hand2")
chat_box.config(state=DISABLED)
chat_box.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

while True:
    if 1==1:
        break



root.mainloop()
