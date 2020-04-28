import tkinter as tk
from tkinter import messagebox
import threading
from serialData import portScales


def listTkUpdate(pScale, listTk):
    update = [False, False]
    while True:
        if pScale.readContin:
            update[0] = pScale.readUpdate
            if update[0] != update[1]:
                listTk.insert(tk.END, pScale.accumulatedMass)
                update[1] = update[0]
        else:
            break


def stopRead(pScale):
    pScale.stopRead()


def startReadWeight(fan, fan_args, pScale, listTk):
    pScale.startRead()
    read = threading.Thread(target=fan, args=fan_args)
    readUbdate = threading.Thread(
        target=listTkUpdate,
        args=(pScale, listTk)
    )
    readUbdate.start()
    read.start()


def main():
    root = tk.Tk()

    pScale = portScales()
    if len(pScale.portsNames) == 0:
        messagebox.showinfo(
            title='Авария',
            message='беда беда завите киповца, не найден COM-port'
        )
    activPort = tk.IntVar()
    portSelection = [
        tk.Radiobutton(
            text=f'для получения данных от весов использовать {x}',
            variable=activPort, value=i
        ) for i, x in enumerate(pScale.portsNames)
    ]
    for x in portSelection:
        x.pack()

    listTk = tk.Listbox(root, width=150, height=20)
    listTk.pack(side=tk.RIGHT)
    frame = tk.Frame(root)
    frame.pack(side=tk.LEFT)
    buttonStart = tk.Button(
        frame, text='Старт',
        command=lambda: startReadWeight(
            pScale.readData,
            (pScale.portsNames[activPort.get()],),
            pScale,
            listTk
        )
    )
    buttonStop = tk.Button(
        frame, text='Стоп',
        command=lambda: stopRead(pScale)
    )
    buttonZeroing = tk.Button(frame, text='Обнулить')
    buttonStart.pack()
    buttonStop.pack()
    buttonZeroing.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
