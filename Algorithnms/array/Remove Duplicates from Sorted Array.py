# coding=utf-8
import time
'''leetcode 26'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global arr
        arr = list(set(nums))
        # k = 0
        # for i in range(1,len(nums)):
        #     if nums[k] != nums[i]:
        #         k += 1
        #         nums[k] = nums[i]
        #     else:
        #         continue
        # return k+1

sol = Solution()
arr = [1,1,2]
print(sol.removeDuplicates(arr))
print(arr)