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
    '''3路排序'''
    rand = random.randint(l, r)
    arr[l], arr[rand] = arr[rand], arr[l]
    v = arr[l]
    '''arr[l+1...lt]<v'''
    lt = l
    '''arr[gt...r]<v'''
    gt = r+1
    '''arr[lt+1...i)==v'''
    i = l+1
    while i<gt:
        if arr[i]<v:
            arr[i],arr[lt+1] = arr[lt+1],arr[i]
            lt+=1
            i+=1
        elif arr[i] >v:
            arr[i],arr[gt-1] = arr[gt-1],arr[i]
            gt-=1
        else:
            i+=1
    arr[l],arr[lt] = arr[lt],arr[l]
    lt-=1
    __quickSort(arr,l,lt)
    __quickSort(arr,gt,r)

# def __quickSort(arr,l,r):
#     if l>=r:
#         return
#     rand = random.randint(l,r)
#     arr[l],arr[rand] = arr[rand],arr[l]
#     v = arr[l]
#     lt = l
#     gt = r+1
#     i=l+1
#     while i<gt:
#         if arr[i] < v:
#             arr[i],arr[lt+1] = arr[lt+1],arr[i]
#             lt+=1
#             i+=1
#         elif arr[i] > v:
#             arr[i],arr[gt-1] = arr[gt-1],arr[i]
#             gt-=1
#         else:
#             i+=1
#     arr[l],arr[lt] = arr[lt],arr[l]
#     lt-=1
#     __quickSort(arr,l,lt)
#     __quickSort(arr,gt,r)

'''三路快速排序不只返回一个，所以我们把它不另写成一个函数。'''
# def __partition(arr,l,r):
#     rand = random.randint(l, r)
#     arr[l], arr[rand] = arr[rand], arr[l]
#     v = arr[l]
#     j = l
#     for i in range(l+1,r+1):
#         if arr[i] < v:
#             arr[j+1],arr[i] = arr[i],arr[j+1]
#             j+=1
#     arr[j],arr[l] = arr[l],arr[j]
#     return j

start = time.time()
arr = generateRandomArray(100000, 0, 100000)
quickSort(arr, len(arr))
print(arr)
print(time.time()-start)

