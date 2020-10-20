from time import sleep
from threading import Thread, Timer


def run_later(message):
    print(message, flush=True)


# t = Timer(1, run_later, kwargs={"message": "hello"})
# t.start()
# t.join()


import sched

s = sched.scheduler()
s.enter(4, 2, run_later, kwargs={"message": "cool, i am schedued"})
s.enter(4, 1000, run_later, kwargs={"message": "cool, i am schedued"})

t = Thread(target=s.run)
t.start()


print("i am doing other sutff", flush=True)


t.join()
