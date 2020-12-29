import threading
import time


def count_one():
    num = 0
    for i in range(1000000):
        num += i

    print(num)


def count_two():
    num = 0
    for i in range(1000000):
        num += i

    print(num)


def main():

    s_t = time.time()
    for i in range(2):
        thread = threading.Thread(target=count_one)
        thread.start()
        thread.join()
    e_t = time.time()
    print("count one time %s" % (e_t - s_t))

    s_t_t = time.time()
    count_two()
    e_t_t = time.time()
    print("count two time %s" % (e_t_t - s_t_t))


if __name__ == '__main__':
    main()

    print("sssaaasadasdasd")

    
    print("Aaaaaaaa")

    print("aaaaa")
    print("ssssssssssss")
