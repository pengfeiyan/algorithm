# coding=utf-8
import random
'''优先队列：出队顺序和入队顺序无关，和优先级有关，而且是动态的'''

'''二叉堆，最大堆，必须是一个完全二叉树，且父节点不小于子节点'''

class MaxHeap:
    '''初始化堆，每次调用insert'''
    # def __init__(self):
    #     self.heap = [None]
    #     self.count = 0

    '''优化堆初始化，每个叶子都可以看成是一个最大堆，只需要对count/2开始的元素进行shiftDown就可以了'''
    '''这个过程叫heapify'''
    # def __init__(self,arr):
    #     self.count = len(arr)
    #     self.heap = [x for x in arr]
    #     self.heap.insert(0,None)
    #     for i in range(self.count//2,0,-1):
    #         self.__shiftDown(i)

    '''原地堆排序，下标从0开始了'''
    def __init__(self,arr,n):
        self.count = len(arr)
        self.heap = [x for x in arr]
        for i in range((self.count-1)//2,-1,-1):
            self.__shiftDown1(arr,n,i)

        n = self.count-1
        for i in range(n,0,-1):
            arr[0],arr[i] = arr[i],arr[0]
            self.__shiftDown1(arr,i,0)

    def __shiftDown1(self,arr,n,k):
        while 2*k+1 < n:
            '''j为和k交换的位置'''
            j = 2*k+1
            if j+1 < n and arr[j+1]>arr[j]:
                j+=1
            if arr[k] >= arr[j]:break
            arr[k],arr[j] = arr[j],arr[k]
            k = j
        return

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def insert(self,item):
        self.count += 1
        self.heap.append(item)
        self.__shiftUp(self.count)

    def __shiftUp(self,count):
        while count>=2 and self.heap[count//2] < self.heap[count]:
            self.heap[count//2],self.heap[count] = self.heap[count],self.heap[count//2]
            count = count//2

    def getMax(self):
        if self.count > 0:
            v = self.heap[1]
            self.heap[1] = self.heap[self.count]
            self.count-=1
            self.heap.pop()
            self.__shiftDown(1)
            return v
        return False

    def __shiftDown(self,k):
        while 2*k<=self.count:
            '''j为和k交换的位置'''
            j = 2*k
            if j+1<=self.count and self.heap[j+1]>self.heap[j]:
                j+=1
            if self.heap[k] >= self.heap[j]:break
            self.heap[k],self.heap[j] = self.heap[j],self.heap[k]
            k = j
        return

if __name__ == '__main__':
    arr = [random.randint(0,100000) for i in range(100000)]
    print(arr)

    heap = MaxHeap()
    for i in arr:
        heap.insert(i)
    arr = []
    while not heap.isEmpty():
        arr.append(heap.getMax())
    print(arr)
