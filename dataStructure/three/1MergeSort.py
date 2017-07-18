# coding=utf-8
from imooc.dataStructure.two.RandomTestcase import *

'''时间复杂度是O(nlogn)'''

''' 测试算法的性能 '''
def testSort(sortName, sortfunc, l, r):
    start = time.time()
    sortfunc(arr,l, r)
    end = time.time()
    # assert (isSorted(arr, n))
    print("%s:%f" % (sortName, end-start))
    return

# def mergeSort(arr,l,r):
#     # if l >= r:
#     #     return
#     ''' 当数量级小的时候，n^2的常数是小于nlogn的，所以当数量及小的时候，可以使用插入排序进行优化'''
#     if r-l<=50:
#         for k in range(l+1,r+1):
#             key = arr[k]
#             index = k
#             while index>l and arr[index-1]>key:
#                 arr[index] = arr[index-1]
#                 index-=1
#             arr[index] = key
#         return
#
#     mid = (l+r)//2
#     mergeSort(arr,l,mid)
#     mergeSort(arr,mid+1,r)
#     ''' 当mid位置的数小于mid+1的位置的话，说明就已经是有序的了，就不需要再排序了 '''
#     if arr[mid] > arr[mid+1]:
#         merge(arr,l,mid,r)
#
# def merge(arr,l,mid,r):
#     # aux = []
#     # for i in arr:
#     #     aux.append(i)
#     '''for循环在pvm中速度太慢，用列表解析，在编译器中以C语言的运行速度编译的，速度明显快了很多'''
#     aux = [x for x in arr]
#     '''必须用深拷贝，不能用浅拷贝'''
#     # aux = arr
#     i = l
#     j = mid+1
#     for k in range(l,r+1):
#         if i > mid:
#             arr[k] = aux[j]
#             j+=1
#         elif j > r:
#             arr[k] = aux[i]
#             i+=1
#         elif aux[i] < aux[j]:
#             arr[k] = aux[i]
#             i+=1
#         else:
#             arr[k] = aux[j]
#             j+=1

def mergeSort(arr,l,r):
    if l>=r:
        return
    mid = (l+r)//2
    mergeSort(arr,l,mid)
    mergeSort(arr,mid+1,r)
    if arr[mid]>arr[mid+1]:
        merge(arr,l,mid,r)

def merge(arr,l,mid,r):
    aux = [x for x in arr]
    i=l
    j=mid+1
    for k in range(l,r+1):
        if i>mid:
            arr[k] = aux[j]
            j+=1
        elif j>r:
            arr[k] = aux[i]
            i+=1
        elif aux[i] < aux[j]:
            arr[k] = aux[i]
            i+=1
        else:
            arr[k] = aux[j]
            j+=1

arr = generateRandomArray(100,0,10000)
mergeSort(arr,0,len(arr)-1)
print(arr)
testSort('mergeSort',mergeSort,0,len(arr)-1)

