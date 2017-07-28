'''快速排序的应用'''
# coding = utf-8
import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        l,r = 0,len(nums)-1
        p = self.partition(nums,l,r)
        while len(nums)-p != k:
            if len(nums)-p < k:
                p = self.partition(nums,l,p-1)
            elif len(nums)-p > k:
                p = self.partition(nums,p+1,r)
        return nums[p]

    def partition(self,nums,l,r):
        i = random.randint(l,r)
        nums[l],nums[i] = nums[i],nums[l]
        key = nums[l]
        j = l
        for i in range(l+1,r+1):
            if nums[i] < key:
                nums[i],nums[j+1] = nums[j+1],nums[i]
                j += 1
        nums[j],nums[l] = nums[l],nums[j]
        return j

sol = Solution()
nums = [6,3,5,2,0,9,7,4,1]
p = sol.findKthLargest(nums,8)
print(p)
