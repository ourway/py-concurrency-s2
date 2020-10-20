from time import sleep
from threading import Thread, Barrier
import queue

b = Barrier(2, timeout=30)

q = queue.Queue()


def some_setup_process():
    print("I am going to create the setup", flush=True)
    sleep(3)  # do something
    print("i am done setting up")
    b.wait()
    # create database connections and ...


def worker():
    print(" i am doing something not important", flush=True)

    # i need to make sure setup process in finished
    b.wait()
    print("i am inserting data", flush=True)


tasks = []
for each in (worker, some_setup_process):
    t = Thread(target=each)
    t.start()
    tasks.append(t)

for t in tasks:
    t.join()
