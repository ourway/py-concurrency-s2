from time import sleep
from threading import Thread, Barrier
import queue


q = queue.Queue()


def some_setup_process():
    print("I am going to create the setup", flush=True)
    sleep(3)  # do something
    print("i am done setting up")
    q.put("lock")
    # create database connections and ...


def worker():
    print(" i am doing something not important", flush=True)

    # i need to make sure setup process in finished
    q.get()
    print("i am inserting data", flush=True)


tasks = []
for each in (worker, some_setup_process):
    t = Thread(target=each)
    t.start()
    tasks.append(t)

for t in tasks:
    t.join()
