import multiprocessing
import os
import time

class A:
    def __init__(self):
        print('class A init')


def f1(s):
    print(f's = {s} , pid = {os.getpid()} , ppid = {os.getppid()}')
    for i in range(0, 100):
        print(s)
        time.sleep(0.1)



# multiprocessing with parameter
if __name__ == '__main__':
    #
    a = A()
    print(a)
    task01 = multiprocessing.Process(target=f1, args=('m',))
    task02 = multiprocessing.Process(target=f1, args=('n',))

    task01.start()
    task02.start()


