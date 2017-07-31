#coding=utf-8
import collections,time
'''leetcode 217 查找表'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        old = len(nums)
        print("old=",old)
        new = len(set(nums))
        print("new=",new)
        return old != new


sol = Solution()

arr = [1,5,9,8,4,6,3,2,7,]
arr1 = set(arr)
start = time.time()
for i in range(1000000):
    max(arr)
    min(arr)
print("list:",time.time()-start)
start1 = time.time()
for i in range(1000000):
    max(arr1)
    max(arr1)
print("set:", time.time()-start1)

#print(sol.containsDuplicate(arr))