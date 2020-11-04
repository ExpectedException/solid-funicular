import concurrent.futures
import logging
import queue
import random
import threading
import time
import numpy as np


class ProducerThread(threading.Thread):
    def run(self):
        global queue
        cnt = 0
        while True:
            if cnt > 7:
                return
            arr = np.random.randint(100, size=10)
            logging.info("Producer got : %s", arr)
            condition.acquire()
            queue.append(arr)
            condition.notify()
            condition.release()
            time.sleep(0.1)
            cnt += 1


class ConsumerThread(threading.Thread):
    def run(self):
        global queue
        cnt = 0.0
        while True:
            if cnt > 7:
                return
            condition.acquire()
            if not queue:
                print("Nothing in queue, consumer will wait.")
                condition.wait()
                print("Producer added something to queue - consumer will stop waiting.")
            arr = queue.pop(0)
            array = np.array(arr)
            print("Consumed", (array[1:] + array[:-1]).max())
            logging.info("Consumer received event. Exiting")
            condition.release()
            time.sleep(0.1)
            cnt += 1


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    condition = threading.Condition()
    queue = []
    ProducerThread().start()
    ConsumerThread().start()