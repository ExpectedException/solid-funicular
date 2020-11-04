import os
import threading
import logging
import time


def _1_():
    logging.info("Thread 1: starting")
    os.system('python checker1.py')
    logging.info("Thread 1: finishing")


def _2_():
    logging.info("Thread 2: starting")
    os.system('python checker2.py')
    logging.info("Thread 2: finishing")


def _3_():
    logging.info("Thread 3: starting")
    os.system('python checker3.py')
    logging.info("Thread 3: finishing")


def _4_():
    logging.info("Thread 4: starting")
    os.system('python checker4.py')
    logging.info("Thread 4: finishing")


def _5_():
    logging.info("Thread 5: starting")
    os.system('python checker5.py')
    logging.info("Thread 5: finishing")


def _6_():
    logging.info("Thread 6: starting")
    os.system('python checker6.py')
    logging.info("Thread 6: finishing")


def _7_():
    logging.info("Thread 7: starting")
    os.system('python checker7.py')
    logging.info("Thread 7: finishing")


def _8_():
    logging.info("Thread 8: starting")
    os.system('python checker8.py')
    logging.info("Thread 8: finishing")


def _9_():
    logging.info("Thread 9: starting")
    os.system('python checker9.py')
    logging.info("Thread 9: finishing")


def _10_():
    logging.info("Thread 10: starting")
    os.system('python checker10.py')
    logging.info("Thread 10: finishing")


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    t1 = threading.Thread(name="1", target=_1_)
    t2 = threading.Thread(name="2", target=_2_)
    t3 = threading.Thread(name="3", target=_3_)
    t4 = threading.Thread(name="4", target=_4_)
    t5 = threading.Thread(name="5", target=_5_)
    t6 = threading.Thread(name="6", target=_6_)
    t7 = threading.Thread(name="7", target=_7_)
    t8 = threading.Thread(name="8", target=_8_)
    t9 = threading.Thread(name="9", target=_9_)
    t10 = threading.Thread(name="10", target=_10_)
    t1.start()
    time.sleep(5)
    t2.start()
    time.sleep(5)
    t3.start()
    time.sleep(5)
    t4.start()
    time.sleep(5)
    t5.start()
    time.sleep(5)
    t6.start()
    time.sleep(5)
    t7.start()
    time.sleep(5)
    t8.start()
    time.sleep(5)
    t9.start()
    time.sleep(5)
    t10.start()
