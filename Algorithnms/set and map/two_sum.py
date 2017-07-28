# coding=utf-8

'''leetcode 1'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if i+1<len(nums) and target-nums[i] in nums[i+1:]:
                return [nums.index(nums[i]),(nums[i+1:].index(target-nums[i]))+i+1]
        return []

sol = Solution()
arr= [3,3,3]
print(sol.twoSum(arr,6))
