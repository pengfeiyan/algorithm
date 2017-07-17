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

# def merge(arr,l,mid,r):
#     aux = []
#     for i in arr:
#         aux.append(i)
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
#
# def mergeSort(arr,l,r):
#     if l >= r:
#         return
#     mid = (l+r)//2
#     mergeSort(arr,l,mid)
#     mergeSort(arr,mid+1,r)
#     merge(arr,l,mid,r)

def mergeSort(arr,l,r):
    if l >= r:
        return
    mid = (l+r)//2
    mergeSort(arr,l,mid)
    mergeSort(arr,mid+1,r)
    merge(arr,l,mid,r)

def merge(arr,l,mid,r):
    aux = []
    for i in arr:
        aux.append(i)
    '''必须用深拷贝，不能用浅拷贝'''
    # aux = arr
    i = l
    j = mid+1
    for k in range(l,r+1):
        if i > mid:
            arr[k] = aux[j]
            j+=1
        elif j > r:
            arr[k] = aux[i]
            i+=1
        elif aux[i] < aux[j]:
            arr[k] = aux[i]
            i+=1
        else:
            arr[k] = aux[j]
            j+=1

arr = generateRandomArray(1000,0,1000)
mergeSort(arr,0,len(arr)-1)
print(arr)
testSort('mergeSort',mergeSort,0,len(arr)-1)


