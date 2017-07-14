# coding=utf-8
import random,time
# 生成n个元素的随机列表，每个元素的随机范围为[rangeL,rangeR]
def generateRandomArray(n,rangeL,rangeR):
    if rangeL > rangeR:
        return None
    arr = []
    for i in range(n):
        arr.append(random.randint(rangeL,rangeR))
    return arr

def isSorted(arr,n):
    for i in range(1,n):
        if arr[n-1] > arr[n]:
            return False
    return True