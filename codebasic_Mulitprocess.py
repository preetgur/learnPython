"""
Author : Gurpreet Singh
Date : 17 jan 2020
purpose : Understand the concept of sharing Data between process using Array and value
"""

"""
###################################
Every Process has its own address space (virtual memory). Thus program variables are not shared between two proecesss. You need to use interprocess communication (IPC) techniques if you want to share data between two  process.
    => IPC Techniques:
    1.Shared Memory : Array,Value
    2.Queue
    3.File

###################################
# Access the varibles bw two process using shared memory [ Varible reside outside of both the processes]
=> One Way using : Array : 
{
 i : integer, d: double 
 3 : size  
 Result  = mulitprocessing.Array('i',3)      # Declaring the Global variable 
}

=> Second Way using : Value  [just single value]
{
    0.0 : single value                # initialize the value
    d : double integer
    v = multiprocessing.Value('d',0.0)

}


"""
import time
import multiprocessing

cube_result = []  # gobal varible (Main-Process)


def calc_square(numbers, shared_result, shared_value):
    print(f'prints numbers : {numbers} and shared_result : {shared_result[:]} and shared_value : {shared_value.value}')
    # print(dir(shared_value))
    shared_value.value = 5.56         #override the varibel of main process  
    # Acessing varible inside the processs p1 and availabel to all processes
    print("Calculate Square of Numbers :")
    
    # when we use "enumerate() fxn" we get both the "index" and "value"
    for index, value in enumerate(numbers):
        shared_result[index] = value * value                # initilize the "Shared_result array"
    print(f"### Copy the array : {shared_result[:]}")

def calc_cube(numbers):
    global cube_result  # p1 process create the copy of varible and this wont be acessibel outside the process p1

    print("Calculate Cube of Numbers :")
    for n in numbers:
        time.sleep(4)  # Delay of Two Seconds
        print(f"Cube : {n*n*n}")
        cube_result.append(n * n * n)
    print(f"within a process : Result : {cube_result}")


if __name__ == "__main__":
    arr = [2, 5, 8, 9]

    # created Array : shared memory [Varible store in memory addresss which is global and access by any proces]
    shared_result = multiprocessing.Array('i', 4)
    print(f'########## This is empy array  : {shared_result}')

    # created Value : shared memory [It store the value it self]
    shared_value = multiprocessing.Value('d', 5.0)

    # Passing the share memory to another process "Array" and "Value" in calc_square function 
    p1 = multiprocessing.Process(target=calc_square, args=(arr, shared_result,shared_value))

    p2 = multiprocessing.Process(target=calc_cube, args=(arr, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done!")

    # A way to print the all the elements in array
    print(f"#### output from square : {shared_result[:]} and output value : {shared_value.value}")

    print(f"#### Result outside of Cube : process : {cube_result}")
    # Becaue every process uses its own memory address
