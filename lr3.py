import logging
import threading
import time
import numpy as np
from readerwriterlock import rwlock
from contextlib import contextmanager
from threading  import Lock
from array import *


class RWLock(object):

    def __init__(self):

        self.w_lock = Lock()
        self.num_r_lock = Lock()
        self.num_r = 0

    def r_acquire(self):
        self.num_r_lock.acquire()
        self.num_r += 1
        if self.num_r == 1:
            self.w_lock.acquire()
        self.num_r_lock.release()

    def r_release(self):
        assert self.num_r > 0
        self.num_r_lock.acquire()
        self.num_r -= 1
        if self.num_r == 0:
            self.w_lock.release()
        self.num_r_lock.release()

    @contextmanager
    def r_locked(self):
        try:
            self.r_acquire()
            yield
        finally:
            self.r_release()

    def w_acquire(self):
        self.w_lock.acquire()

    def w_release(self):
        self.w_lock.release()

    @contextmanager
    def w_locked(self):
        try:
            self.w_acquire()
            yield
        finally:
            self.w_release()


def write1():
    global arr
    while(True):
        with a.w_locked():
            time.sleep(0.2)
            arr.insert(0, np.random.randint(100, size=10))
            logging.info("Write 1 : %s", arr[0])


def write2():
    global arr
    while(True):
        with a.w_locked():
            time.sleep(0.3)
            arr.insert(1, np.random.randint(100, size=10))
            logging.info("Write 2 : %s", arr[1])


def write3():
    global arr
    while(True):
        with a.w_locked():
            time.sleep(0.4)
            arr.insert(3, np.random.randint(100, size=10))
            logging.info("Write 3 : %s", arr[2])


def write4():
    global arr
    while(True):
        with a.w_locked():
            time.sleep(0.5)
            arr.insert(4, np.random.randint(100, size=10))
            logging.info("Write 4 : %s", arr[3])


def read1():
    global arr
    while(True):
        time.sleep(1)
        with a.r_locked():
            time.sleep(0.2)
            print("MIN 1: ", np.array(arr[0]).min())
            print("MIN 3: ", np.array(arr[2]).min())
            logging.info("Read 1. Exiting")


def read2():
    global arr
    while(True):
        time.sleep(1)
        with a.r_locked():
            time.sleep(0.3)
            print("MIN 2: ", np.array(arr[1]).min())
            print("MIN 4: ", np.array(arr[3]).min())
            logging.info("Read 2. Exiting")


if __name__ == "__main__":
    a = RWLock()
    arr = []
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    threading.Thread(target=write1,).start()
    threading.Thread(target=write2, ).start()
    threading.Thread(target=write3, ).start()
    threading.Thread(target=write4, ).start()
    threading.Thread(target=read1,).start()
    threading.Thread(target=read2, ).start()
