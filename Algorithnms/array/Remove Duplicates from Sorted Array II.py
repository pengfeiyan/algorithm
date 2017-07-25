# coding=utf-8

''' leetcode 80'''
class Solution(object):
    def removeDuplicates(self, nums):
        tail = 0
        for num in nums:
            if tail < 2 or num != nums[tail - 1] or num != nums[tail - 2]:
                nums[tail] = num
                tail += 1
        return tail



sol = Solution()
arr = [1,1,1,2,2,2,3]
i = sol.removeDuplicates(arr)
print(arr[0:i])

