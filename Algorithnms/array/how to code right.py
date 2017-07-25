# coding=utf-8

def binarySearch(arr,n,target):
    '''arr[l...r]查找target'''
    l,r = 0,n-1
    '''当l==r时，[l...r]依然是有效的'''
    while l<=r:
        mid = l+(r-l)//2
        if (arr[mid] == target):
            return mid
        elif arr[mid] < target:
            l = mid+1
        else:
            r = mid-1
    return -1