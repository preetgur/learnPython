"""
Authour : Gurpreet Singh
Date : 17 Jan 2020
Purpose : For a given list of numbers print square and cube  of every numbers

"""
# Multi Threading  : Execution in paralel


import time
import threading


def calc_square(numbers):
    print("Calculate Square of Numbers :")
    for n in numbers:
        time.sleep(2)  # Delay of Two Seconds
        print(f"Square : {n*n}")


def calc_cube(numbers):
    print("Calculate Cube of Numbers :")
    for n in numbers:
        time.sleep(2)  # Delay of Two Seconds
        print(f"Cube : {n*n*n}")


if __name__ == "__main__":

    arr = [2, 8, 9, 3]

    print("########## Simple Exceution of Function ##########")
    t = time.time()
    calc_square(arr)
    calc_cube(arr)
    time1 = time.time() - t  # Calculate difference in time
    print(f"Done in : {time1}")

    print("########## Thread Exceution of Function ##########")
    t = time.time()
    t1 = threading.Thread(target=calc_square, args=(arr, ))
    t2 = threading.Thread(target=calc_cube, args=(arr, ))

    # Starts the execution of Threads
    t1.start()
    t2.start()

    # Merge to the main Threads
    t2.join()
    t2.join()
    time2 = time.time() - t
    print(f"Done in : {time2}")
    print(".. I am done with all my work now ! ")

    print(
    f"##### Difference In Execution Time ###### \nsimple Exceution Time {time1} \nThread Exceution Time {time2}"
    )
