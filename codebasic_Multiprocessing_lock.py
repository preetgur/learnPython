"""
Author : Gurpreet Singh
Date : 17 jan 2020
Purpose : To Understand the concept of locking in Mulitprocessing

################
Multiprocessing Lock : is used to resist that two process cannot use the same memeory location at the same time [ which leads the program is confliction ].

############
create lock varible

    lock = multiprocessing.Lock()   

    lock.acquire()    # lock is activate
    lock.release()    # lock is deactivate

"""

import time
import multiprocessing

# First Child Process
def deposit(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

# Second Child Process
def withdraw(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()


if __name__ == "__main__":
    balance = multiprocessing.Value('i',200) #shared variable

    lock = multiprocessing.Lock()   # create lock varible
    d = multiprocessing.Process(target=deposit, args=(balance,lock))
    w = multiprocessing.Process(target=withdraw, args=(balance,lock))

    d.start()
    w.start()

    d.join()
    w.join()

    print(balance.value)