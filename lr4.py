import threading
import numpy as np
import time
import logging


def convolution():
    global arr
    lst = []
    logging.debug('Locked')
    lock.acquire()
    try:
        High = len(arr)
        for i in range(0, High, 2):
            lst.append(np.fmax(arr[i], arr[i+1]))
            time.sleep(0.01)
        print(lst)
        print(len(lst))
        arr = lst
    finally:
        logging.debug('Unlocked')
        lock.release()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='(%(threadName)-1s) %(message)s', )
    lock = threading.Lock()
    global arr
    arr = np.random.randint(100, size=1024)
    event = threading.Event()
    ThCount = 10
    for t in range(ThCount):
        #threading.Thread(target=convolution, args=(lst, (le/ThCount)*t, (le/ThCount)*(t+1), )).start()
        threading.Thread(target=convolution).start()


