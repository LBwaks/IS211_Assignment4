import time


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


def python_sort():
    pass


def main():
    pass
