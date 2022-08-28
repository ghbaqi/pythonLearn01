

# 不带参数的 多进程任务
import multiprocessing
import time


def f1():
    for i in range(0, 100):
        print ('a')
        time.sleep(0.1)

def f2():
    for i in range(0, 100):
        print ('b')
        time.sleep(0.1)


if __name__ == '__main__':
    task01 = multiprocessing.Process(target=f1)
    task02 = multiprocessing.Process(target=f2)

    task01.start()
    task02.start()
