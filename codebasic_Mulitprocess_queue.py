"""
Author : Gurpreet Singh
Date : 17 jan 2020
Purpose : To understand how to access the varible of one process to another using "Queue"

######################
Queue : FIFO (First in First out)
Two Method : 
put : enqueue
get : dequeue

###############
Create Queue varible :
q = muliiprocessing.Queue()

"""

import time
import multiprocessing

def calc_square(numbers,q):
    
    for i in numbers:
        q.put(i*i)      #Put the element in the End of queue 


if __name__ == "__main__":
    arr = [2, 5, 8, 9]
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=calc_square, args=(arr,q))

    p1.start()
    p1.join()
    
# when queue is empty it return "true" and condition valus
    while q.empty() is False:
        print(q.empty()) 
        print(q.get())

""" 
Difference bw Multiprocessing Queue and "Queue Module"
###################

import multiprocessing
q = muliprocessing.Queue()

{
    Lives in shared memory
    used to share data between processes
}

################

import queue
q = queue.Queue()

{
    lives in in-process memeory
    used to share data between thereads
}

"""        
