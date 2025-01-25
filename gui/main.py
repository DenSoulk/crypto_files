import tkinter as tk
from tkinter import ttk

main_window = tk.Tk()
main_window.title("Crypto messenger")
main_window.geometry("500x500")


button = tk.Button(main_window, text="Baton", command=None)
button.pack()
entry = tk.Entry(main_window)
entry.pack()
label = tk.Label(main_window, text="login")
label.pack()




main_window.mainloop()

