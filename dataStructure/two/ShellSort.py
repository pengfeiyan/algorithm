# coding=utf-8
from imooc.dataStructure.two.RandomTestcase import *

'''shell排序是插入排序的优化,时间复杂度最差是O(n^2),最好和插入排序一样是O(n),平均是O(n^3/2)'''

''' 测试算法的性能 '''
def testSort(sortName, sortfunc, arr, n):
    start = time.time()
    sortfunc(arr, n)
    end = time.time()
    # assert (isSorted(arr, n))
    print("%s:%f" % (sortName, end-start))
    return

def shellSort(arr,n):
    step = 0
    while step <= n/3:
        '''选取3n+1的步长'''
        step = step*3+1
    while step > 0:
        for i in range(step,n):
            key = arr[i]
            j=i
            while j > 0 and arr[j-step] > key:
                arr[j] = arr[j-step]
                j-=step
            arr[j] = key

        step = (step-1)//3

arr = generateRandomArray(10000,0,10000)
testSort('shellsort',shellSort,arr,len(arr))
# shellSort(arr,len(arr))
# print(arr)