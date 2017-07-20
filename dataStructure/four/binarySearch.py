# coding=utf-8

''' 数组必须是有序的'''

def binarySearch(arr,n,target):
    '''在arr[l...r]'''
    l,r = 0,n-1
    while l<=r:
        ''' l+r 特别大的时候，会有溢出的可能'''
        # mid = (l+r)//2
        mid = l+(r-l//2)
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            r = mid-1
        else:
            l = mid+1
    return -1

def binarySearch1(arr,l,r,target):
    if l>r:
        return False
    mid = l+(r-l)//2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binarySearch1(arr,l,mid-1,target)
    else:
        return binarySearch1(arr,mid+1,r,target)


arr = [1,2,3,4,5,6,7,8,9,10]
print(binarySearch1(arr,0,len(arr)-1,1))