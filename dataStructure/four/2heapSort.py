# coding =utf-8
from imooc.dataStructure.four.heap import *
from imooc.dataStructure.two.RandomTestcase import generateRandomArray
import time

# def heapSort(arr,n):
#     heap = MaxHeap(arr)
#     for i in arr:
#         heap.insert(i)
#     arr = []
#     print(heap.heap)
#     while not heap.isEmpty():
#         arr.append(heap.getMax())
#     print(arr[::-1])

# start = time.time()
# arr = generateRandomArray(10,0,100)
# heapSort(arr,len(arr))
# print(time.time()-start)

arr = generateRandomArray(10,0,100)
heap = MaxHeap(arr,len(arr))
print(heap.heap)
print(arr)

