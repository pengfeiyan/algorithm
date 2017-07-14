# coding = utf-8
''' 算法复杂度为O(n^two) '''

def selectionSort(arr,n):
    for i in range(n):
        ''' 寻找[i,n)中最小值的下标'''
        minIndex = i
        for j in range(i+1,n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        '''交换最小值'''
        arr[i],arr[minIndex] = arr[minIndex],arr[i]


arr = [8,6,2,3,1,5,7,4]
selectionSort(arr,len(arr))
for i in arr:
    print(i)