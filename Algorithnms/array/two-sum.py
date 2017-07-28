'''leetcode 1'''
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     if i+1<len(nums) and target-nums[i] in nums[i+1:]:
        #         a = nums.index(nums[i])
        #         b = (nums[i+1:].index(target-nums[i]))+i+1
        #         return [a,b]
        # return []

        dic = {}
        for index,value in enumerate(nums):
            dic[value] = index

        for i in range(len(nums)):
            if target != 2*nums[i] and target-nums[i] in dic:
                return [i,dic[target-nums[i]]]
        return []


sol = Solution()
arr = [3,2,4]
print(sol.twoSum(arr,6))