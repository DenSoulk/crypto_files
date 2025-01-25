import json
from tkinter import *
import tkinter
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

def send_message():
    message = entry.get()
    if message:
        chat_box.config(state=tkinter.NORMAL)
        chat_box.insert(END, f"You: {message}\n")
        chat_box.config(state=tkinter.DISABLED)
        # save_message(message)
        entry.delete(0, END)

root = Tk()
root.title("Your chat")


send_button = Button(root, text="Отправить", command=send_message, cursor="hand2")
send_button.pack(side=RIGHT, anchor=SE, fill=X, padx=5, pady=5)

entry = PlaceholderEntry(root, placeholder="Введите текст")
entry.pack(side=BOTTOM, fill=X, padx=5, pady=5)

chat_box = Text(root, cursor="hand2")
chat_box.config(state=tkinter.DISABLED)
chat_box.pack(side=TOP, fill=BOTH, expand=True, padx = 5, pady = 5) 

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
