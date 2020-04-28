import tkinter as tk
import threading


root = tk.Tk()
listTk = tk.Listbox(root)
listTk.pack(side=tk.RIGHT)
frame = tk.Frame(root)
frame.pack(side=tk.LEFT)
buttonStart = tk.Button(frame, text='Старт')
buttonStop = tk.Button(frame, text='Стоп')
buttonZeroing = tk.Button(frame, text='Обнулить')
buttonStart.pack()
buttonStop.pack()
buttonZeroing.pack()
root.mainloop()
