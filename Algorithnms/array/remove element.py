# coding=utf-8

''' leetcode 27 '''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(0,len(nums)):
            if nums[i] != val:
                if i != k:
                    nums[i],nums[k] = nums[k],nums[i]
                k+=1
        # print(nums[0:k],k)
        return k
sol = Solution()
arr = [3,2,2,3]
sol.removeElement(arr,0)
