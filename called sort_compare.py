import time
import random


def insertion_sort(alist):
    starttime = time.time()
    for index in range(1, len(alist)):
        currentValue = alist[index]
        position = index
        while position > 0 and alist[position - 1] > currentValue:
            alist[position] = alist[position - 1]
            position = position - 1
        alist[position] = currentValue
    endtime = time.time()
    execution_time = endtime - starttime
    return execution_time


def shell_sort(alist):
    starttime = time.time()
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        print("After increments of size", sublistcount, "The list is :", alist)
        sublistcount = sublistcount // 2
    stoptime = time.time()
    executiontime = stoptime - starttime
    return executiontime


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentValue = alist[i]
        position = i
        while position > gap and alist[position - gap] > currentValue:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentValue


def python_sort(alist):
    starttime = time.time()
    alist.sort()
    endtime = time.time()
    execution_time = endtime - starttime
    return execution_time


def main():
    sizes = [500, 1000, 10000]
    for size in sizes:
        num_iterations = 10  # Number of times to run each sorting algorithm
        insertion_total_time = 0
        shell_total_time = 0
        python_total_time = 0

        for _ in range(num_iterations):
            random_list = [random.randint(1, 1000) for _ in range(size)]
            insertion_total_time += insertion_sort(random_list.copy())
            shell_total_time += shell_sort(random_list.copy())
            python_total_time += python_sort(random_list.copy())
        average_insertion_time = insertion_total_time / num_iterations
        average_shell_time = shell_total_time / num_iterations
        average_python_time = python_total_time / num_iterations

        print(f"List Size: {size}")
        print(
            f"Insertion Sort Time took: {average_insertion_time:.6f} seconds to run on average"
        )
        print(
            f"Shell Sort Time took: {average_shell_time:.6f} seconds to run on average"
        )
        print(
            f"Python Sort Time took: {average_python_time:.6f} seconds to run on average"
        )
        print()


if __name__ == "__main__":
    main()
