# coding=utf-8
from imooc.dataStructure.two.RandomTestcase import *
'''冒泡排序的时间复杂度是O(n^2)'''

def bubbleSort(arr,n):
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
            else:
                continue
arr = generateRandomArray(10,0,10)
bubbleSort(arr,len(arr))
print(arr)
