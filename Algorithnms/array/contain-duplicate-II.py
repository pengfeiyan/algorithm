'''leetcode 219 滑动窗口和查找表'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        '''滑动窗口为nums[l...r]'''
        dic = {}
        for index, value in enumerate(nums):
            '''判断值是否在dic中，并且本次下标-上一次的下标小于等于K，说明存在'''
            if value in dic and index - dic[value] <= k:
                return True
            '''上一次出现的值，不满足下标差要求，则更新下标'''
            dic[value] = index
        return False


sol = Solution()
nums = [1,0,1,0,3]
print(sol.containsNearbyDuplicate(nums,1))