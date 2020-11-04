import threading
import numpy as np
import time
import logging


def gen():
    global arr
    arr = np.random.randint(100, size=1024)


def sf(i):
    global arr
    logging.debug('Waiting')
    event[i].wait()
    logging.debug('Working')
    tarr = []
    for q in range(0, int((len(arr)/2))):
        tarr.append(arr[q]+arr[q+int(len(arr)/2)])
    arr = list(tarr)
    time.sleep(0.1)
    logging.debug('Done')
    try:
        event[i+1].set()
    except:
        print(arr)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s: %(message)s (%(threadName)-1s)', )
    gen()
    global event
    event = []
    for i in range(0, 10):
        x = threading.Event()
        event.append(x)
        event[i].clear()
        threading.Thread(target=sf, args=(i, )).start()
    event[0].set()
