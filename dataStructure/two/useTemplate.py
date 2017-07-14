# coding = utf-8
from imooc.dataStructure.two.RandomTestcase import *

''' 算法复杂度为O(n^2) '''

def testSort(sortName, sortfunc, arr, n):
    start = time.time()
    sortfunc(arr, n)
    end = time.time()
    assert (isSorted(arr, n))
    print("%s:%f" % (sortName, end-start))
    return

def selectionSort(arr,n):
    for i in range(n):
        ''' 寻找[i,n)中最小值的下标'''
        minIndex = i
        for j in range(i+1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        '''交换最小值'''
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

arr = generateRandomArray(50, 0, 100000)
#
# func = selectionSort
''' 将一个函数作为参数传入另一个函数中，需要将函数名传进去，然后将参数传进去'''
testSort("selectionSort", selectionSort, arr, len(arr))

selectionSort(arr, len(arr))
for i in arr:
    print(i)