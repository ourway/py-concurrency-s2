from concurrent.futures import ThreadPoolExecutor
from time import sleep


def print_after_5_secs(message):
    sleep(5)
    print(message, flush=True)
    return "wow"


with ThreadPoolExecutor(3) as pool:
    for i in range(10):
        future = pool.submit(print_after_5_secs, ("hello"))
        print(future.done())
        print(future.done())
