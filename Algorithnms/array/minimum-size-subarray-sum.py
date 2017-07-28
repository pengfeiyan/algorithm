# coding=utf-8
'''leetcode 209 滑动窗口'''

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # nums[l...r]
        l,r = 0,-1
        sum = 0
        res = len(nums)+1
        while l < len(nums):
            if sum < s and r+1 < len(nums):
                r += 1
                sum += nums[r]
            else:
                sum -= nums[l]
                l += 1

            if sum >= s:
                res = min(res,r-l+1)
        if res == len(nums)+1:
            return 0
        return res

sol = Solution()
arr = [2,3,1,2,4,3]
s = 8
print(sol.minSubArrayLen(s,arr))

