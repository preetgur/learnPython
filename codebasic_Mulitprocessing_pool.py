""" 
Author : Gurpreet Singh
Date : 17 Jan 2020
Purpose : To understand the concept of  Mulitprocessing Pool

############## 
[Pool speed up your process]

Multiprocessing Pool (Map Reduce) : In this we understand how to use all the "core" of cpu by dividing the input between multiple core [Which is called "Map"] after then collect the resutl from all the cores.[which is called "Reduce"]

we use this becacuse we not want to put the burden on single core but share the code among them.

############
=> importing pool
from multiprocessing import Pool

=> initialize pool object
p = Pool()  

=>  # It divides the program bw all cores of computer : first argument is function :second argrument is iterable 
result = p.map(f,range(10000))

=> close pool
p.close()

=> join to main process
p.join()
"""
from multiprocessing import Pool
import time

def f(n):
    sum = 0
    for i in range(1000):
        sum += i*i
    return sum

if __name__ == "__main__":
    
    t1 = time.time()

    # p = Pool(processes=3)  # it creates 3 process at a time
    p = Pool()        # initialize pool object
    # print(dir(Pool()))
    result = p.map(f,range(100000))  # divides the work bw all cores
    p.close()
    p.join()
    print(f"Pool Processing took : {time.time()- t1} seconds")    

    
    t2 = time.time()
    result = []
    for i in range(100000):
        result.append(f(i))

    print(f"Serial Processing took : {time.time()- t2} seconds")    