# coding=utf-8
from imooc.dataStructure.two.RandomTestcase import *
import random
# def quickSort(arr,n):
#     __quickSort(arr,0,n-1)
#
# ''' arr[l...r]部分快速排序'''
# def __quickSort(arr,l,r):
#     if l>=r:
#         return
#     p = __partition(arr,l,r)
#     __quickSort(arr,l,p-1)
#     __quickSort(arr,p+1,r)
#
# '''arr[l...r]进行分块操作'''
# def __partition(arr,l,r):
#     v = arr[l]
#     j = l
#     for i in range(l+1,r+1):
#         ''' arr[l+1...j]<v,arr[j+1...i-1]>v'''
#         if arr[i] < v:
#             arr[j+1],arr[i] = arr[i],arr[j+1]
#             j+=1
#     arr[l],arr[j] = arr[j],arr[l]
#     return j
'''快速排序在排近乎有序的数列的时候，会退化为几乎是O(n^2)'''

def quickSort(arr,n):
    __quickSort(arr,0,n-1)

def __quickSort(arr,l,r):
    # if l >= r:
    #     return
    ''' 高级排序算法的底层，都可以用基本的排序算法来时间。因为数量级小的时候，n^2的常数要小于nlogn的'''
    if r-l <=15:
        for i in range(l+1,r+1):
            key = arr[i]
            j=i
            while j>l and arr[j-1]>key:
                arr[j] = arr[j-1]
                j-=1
            arr[j] = key
        return
    p = __partition(arr,l,r)
    __quickSort(arr,l,p-1)
    __quickSort(arr,p+1,r)

def __partition(arr,l,r):
    '''为了防止快速排序在排序近乎有序的序列时间复杂度退化为近乎n^2的可能，需要将l位置的元素和一个随机位置的元素交换位置即可。'''
    rand = random.randint(l,r)
    arr[l], arr[rand] = arr[rand],arr[l]
    v = arr[l]
    j = l
    for i in range(l+1,r+1):
        if arr[i] < v:
            arr[j+1],arr[i] = arr[i],arr[j+1]
            j+=1
    arr[j],arr[l] = arr[l],arr[j]
    return j

start = time.time()
arr = generateRandomArray(10000,0,10)
quickSort(arr,len(arr))
print(arr)
print(time.time()-start)