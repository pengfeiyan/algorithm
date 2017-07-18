# coding=utf-8
from imooc.dataStructure.two.RandomTestcase import *

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

def quickSort(arr,n):
    __quickSort(arr,0,n-1)

def __quickSort(arr,l,r):
    if l >= r:
        return
    p = __partition(arr,l,r)
    __quickSort(arr,l,p-1)
    __quickSort(arr,p+1,r)

def __partition(arr,l,r):
    v = arr[l]
    '''j的位置是小于v的部分，包括j'''
    j = l
    '''arr[l+1...j]<v,arr[j+1,i)>v,i为开区间，因为i为正在考察的元素'''
    for i in range(l+1,r+1):
        if arr[i] < v:
            '''i的位置属于小于v的部分，需要将j+1的元素和i位置的交换位置'''
            arr[j+1],arr[i] = arr[i],arr[j+1]
            j+=1
    '''最后将j的位置和最左边的元素交换位置，保证arr[l...j-1]<v,arr[j+1...r]>v'''
    arr[j],arr[l] = arr[l],arr[j]
    return j

start=time.time()
arr = generateRandomArray(100000,0,1000)
quickSort(arr,len(arr))
print(arr)
print(time.time()-start)