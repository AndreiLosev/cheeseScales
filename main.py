import tkinter as tk
from tkinter import messagebox
import threading
from serialData import portScales


def main():
    root = tk.Tk()
    pScale = portScales()
    if len(pScale.portsNames) == 0:
        messagebox.showinfo(
            title='Авария',
            message='беда беда завите киповца, не найден COM-port'
        )
    activPort = tk.BooleanVar
    portSelection = [
        tk.Radiobutton(
            text=f'для получения данных от весов использовать {x, i}',
            variable=activPort, value=i
        ) for i, x in enumerate(pScale.portsNames)
    ]
    for x in portSelection:
        x.pack()
    listTk = tk.Listbox(root, width=150)
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


if __name__ == '__main__':
    main()
