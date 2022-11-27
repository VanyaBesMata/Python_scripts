import tkinter as Tkinter
from datetime import datetime
counter = 0
running = False


def counter_label(label):
    def count():
        if running:
            global counter
            # Начальная задержка.
            if counter == 0:
                display = 'Начало!'
            else:
                tt = datetime.utcfromtimestamp(counter)
                string = tt.strftime('%H:%M:%S')
                display = string

            label['text'] = display

            label.after(1000, count)
            counter += 1

    # Запуск счетчика.
    count()


# Старт.
def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'


# Стоп.
def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False


# Очистка.
def Reset(label):
    global counter
    counter = 0
    # Если очистка нажата после нажатия стоп.
    if not running:
        reset['state'] = 'disabled'
        label['text'] = '00:00:00'
    # Если сброс нажат во время работы.
    else:
        label['text'] = '00:00:00'


root = Tkinter.Tk()
root.title("Секундомер")

# Рабочее окно.
root.minsize(width=250, height=70)
label = Tkinter.Label(root, text='Начало!', fg='black', font='Verdana 30 bold')
label.pack()
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Старт', width=6, command=lambda: Start(label))
stop = Tkinter.Button(f, text='Стоп', width=6, state='disabled', command=Stop)
reset = Tkinter.Button(f, text='Очистка', width=6, state='disabled', command=lambda: Reset(label))
f.pack(anchor='center', pady=5)
start.pack(side='left')
stop.pack(side='left')
reset.pack(side='left')
root.mainloop()