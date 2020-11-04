from tkinter import *
import numpy as np
import threading
import logging
import time
import queue


def click_button():
    logging.debug('CB started')
    t = threading.Thread(target=gen)
    t.start()
    t.join()
    t1 = threading.Thread(target=sum3)
    t1.start()
    t1.join()
    try:
        label2.config(text=arr)
    finally:
        logging.debug('CB finished')


def gen():
    lock.acquire()
    try:
        logging.debug('Gen started')
        global arr
        arr = np.random.randint(100, size=1000)
    finally:
        lock.release()
        logging.debug('Gen finished')


def sum3():
    lock.acquire()
    try:
        logging.debug('Sum3 started')
        global arr
        arr = sum(arr[0:3])
    finally:
        lock.release()
        logging.debug('Sum3 finished')


if __name__ == '__main__':
    q = queue.Queue()
    logging.basicConfig(level=logging.DEBUG,
                            format='(%(threadName)-1s) %(message)s', )
    lock = threading.Lock()
    root = Tk()
    root.title("GUI")
    root.geometry("300x250")

    label2 = Label(text="qwe", justify=LEFT)
    label2.place(relx=0.5, rely=0.5, anchor=CENTER)

    btn = Button(text="Generate", background="#555", foreground="#ccc",
                 padx="20", pady="8", font="16", command=click_button)
    btn.pack()

    root.mainloop()
