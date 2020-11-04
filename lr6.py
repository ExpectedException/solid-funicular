from tkinter import *
import numpy as np
import threading
import logging
import time


def sensor1():
    global buf1
    buf1 = np.random.randint(100, size=5)
    sem1.release()


def sensor2():
    global buf2
    buf2 = np.random.randint(100, size=5)
    sem2.release()
    global buf3
    buf3 = np.random.randint(42, size=5)
    sem3.release()


def sensor3():
    global buf4
    buf4 = np.random.randint(88, size=8)
    sem4.release()


def sensor4():
    global buf5
    buf5 = np.random.randint(100, size=8)
    sem5.release()


def sensors():
    while 1 == 1:
        time.sleep(0.2)
        sensor1()
        time.sleep(0.2)
        sensor2()
        time.sleep(0.2)
        sensor3()
        time.sleep(0.2)
        sensor4()
        time.sleep(0.2)


def ev1():
    while 1 == 1:
        while sem1.acquire(blocking=False):
            tstr = "Sensor 1: " + str(min(buf1))
            label1.config(text=tstr)
            sem1.acquire()


def ev2():
    while 1 == 1:
        if sem2.acquire(blocking=False):
            tstr = "Sensor 2: " + str(min(buf2))
            label2.config(text=tstr)
            sem2.acquire()


def ev3():
    while 1 == 1:
        if sem3.acquire(blocking=False):
            tstr = "Sensor 3: " + str(min(buf3))
            label3.config(text=tstr)
            sem3.acquire()


def ev4():
    while 1 == 1:
        if sem4.acquire(blocking=False):
            tstr = "Sensor 4: " + str(max(buf4))
            label4.config(text=tstr)
            sem4.acquire()


def ev5():
    while 1 == 1:
        if sem5.acquire(blocking=False):
            tstr = "Sensor 5: " + str(max(buf5))
            label5.config(text=tstr)
            sem5.acquire()


def click_button():
    threading.Thread(target=sensors).start()
    threading.Thread(target=ev1).start()
    threading.Thread(target=ev2).start()
    threading.Thread(target=ev3).start()
    threading.Thread(target=ev4).start()
    threading.Thread(target=ev5).start()


if __name__ == '__main__':
    global BufFree, buf1, buf2, buf3, buf4, buf5
    BufFree = [True for i in range(5)]
    logging.basicConfig(level=logging.DEBUG,
                        format='(%(threadName)-1s) %(message)s', )
    sem1 = threading.Semaphore()
    sem2 = threading.Semaphore()
    sem3 = threading.Semaphore()
    sem4 = threading.Semaphore()
    sem5 = threading.Semaphore()
    sem1.acquire()
    sem2.acquire()
    sem3.acquire()
    sem4.acquire()
    sem5.acquire()
    root = Tk()
    root.title("GUI")
    root.geometry("300x250")

    label1 = Label(justify=LEFT)
    label1.place(relx=0.5, rely=0.3, anchor=CENTER)
    label2 = Label(justify=LEFT)
    label2.place(relx=0.5, rely=0.4, anchor=CENTER)
    label3 = Label(justify=LEFT)
    label3.place(relx=0.5, rely=0.5, anchor=CENTER)
    label4 = Label(justify=LEFT)
    label4.place(relx=0.5, rely=0.6, anchor=CENTER)
    label5 = Label(justify=LEFT)
    label5.place(relx=0.5, rely=0.7, anchor=CENTER)

    btn = Button(text="Generate", background="#555", foreground="#ccc",
                 padx="20", pady="8", font="16", command=click_button)
    btn.pack()

    root.mainloop()



