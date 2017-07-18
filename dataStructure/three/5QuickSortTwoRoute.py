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
    rand = random.randint(l,r)
    arr[l], arr[rand] = arr[rand],arr[l]
    v = arr[l]
    '''arr[l+1...i)<=v,arr[j...r]>=v'''
    i,j = l+1,r
    while True:
        '''小于V的会放在l...j中，但是当序列出现大量的重复数据的时候，会造成一部分特别大，也会退化成n^2的'''
        while i<=r and arr[i] < v:
            i+=1
        while j >= l+1 and arr[j] > v:
            j-=1
        if i>j:
            break
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1
    arr[l],arr[j] = arr[j],arr[l]
    return j

start = time.time()
arr = generateRandomArray(100000,0,10000)
quickSort(arr,len(arr))
print(arr)
print(time.time()-start)