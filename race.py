from threading import Thread

counter = 0


def increment():
    global counter
    for _ in range(500000):
        counter += 1


threads = []


def run():
    for _ in range(30):
        t = Thread(target=increment)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("excepted counter value = 150000")
    print("actual = %d" % counter)


run()
