import threading
import time
from queue import Queue

import requests
"""
kafka



rocket mq   
    topic主题  
        producer 写入case  执行 ing
        consumer json格式数据 解析 json
        
        
        
        
        
rabbit mq

"""


def task_get_one(q):



    for i in range(500):
        """
        生产者  50000000
        """

        get = requests.get("http://www.baidu.com")

        q.put(get.status_code)



def task_get_two():

    for i in range(500):


        post = requests.get("http://www.baidu.com")

        code = post.status_code

        print(code)


def main():

    q = Queue()


    s_t = time.time()
    threads = []
    for i in range(1):
        threads.append(threading.Thread(target=task_get_one,args=(q,)))

    for _ in threads:
        _.start()
        _.join()
    print(q.qsize())

    """
    消费者
    """
    print(q.get())

    e_t = time.time()
    print("count one time %s" % (e_t - s_t))

    s_t_t = time.time()
    task_get_two()
    e_t_t = time.time()
    print("count two time %s" % (e_t_t - s_t_t))

if __name__ == '__main__':
    main()

