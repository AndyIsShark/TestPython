import threading


def test():
    print("start one... %s" % threading.current_thread().name)
    num = 0
    for i in range(1000000):
        num += i
    print("end one ... %d" % num)


def test_():
    print("start two... %s" % threading.current_thread().name)
    sum = 0
    for i in range(100000):
        sum += i
    print("end two ... %d" % sum)


if __name__ == '__main__':

    print(threading.current_thread().name)

    threads = []
    thredings = []

    for i in range(5):
        thread = threading.Thread(target=test)
        thread.start()
        threads.append(thread)
    for _ in threads:
        _.join()

    for i in range(5):
        threading_thread = threading.Thread(target=test_)
        threading_thread.start()
        thredings.append(threading_thread)
    for t in thredings:
        t.join()

    print("all thread done...")
