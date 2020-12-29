"""



"""
import threading
from time import sleep

num = 10


def task_one():
    global num
    sleep(5)
    num = 101
    print(str(num) + "    " + "%s" % threading.current_thread().name)


def task_two():
    global num

    num = 102
    print(str(num)+"    "+"%s" %threading.current_thread().name)


def main():
    print(threading.current_thread().name)

    thread = threading.Thread(target=task_one)

    thread.start()
    #
    thread.join()

    threading_thread = threading.Thread(target=task_two)
    threading_thread.start()
    threading_thread.join()




if __name__ == '__main__':
    main()
    print(num)
