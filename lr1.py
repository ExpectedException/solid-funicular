import logging
import threading
import time
from random import random


def average(N):
    logging.info("Main    : thread avg start")
    arr = [0] * N
    for i in range(N):
        arr[i] = int(random() * 100)
    print(arr)
    s = 0
    for i in range(N):
        s += arr[i]
    print(s / N)
    logging.info("Main    : thread avg end")


def fib(N):
    logging.info("Main    : thread fib start")
    arr = [0] * N
    for i in range(N):
        if i == 0:
            arr[i] += 0
        elif i == 1:
            arr[i] += 1
        else:
            arr[i] += arr[i - 1] + arr[i - 2]

    print(arr)
    s = 0
    for i in range(N):
        s += arr[i]
    print(s / N)
    logging.info("Main    : thread fib end")


if __name__ == "__main__":
    N = 30
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")
    x = threading.Thread(target=average, args=(N,))
    y = threading.Thread(target=fib, args=(N, ))
    x.start()
    y.start()
    logging.info("Main    : all done")
