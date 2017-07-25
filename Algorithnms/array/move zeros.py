# coding=utf-8

# leetcode 283
'''
时间复杂度是O(n)
空间复杂度是O(n)
'''

# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         arr = []
#         for i in nums:
#             if i != 0:
#                 arr.append(i)
#         for j in range(0,len(arr)):
#             nums[j] = arr[j]
#
#         for k in range(len(arr),len(nums)):
#             nums[k] = 0

'''
时间复杂度是O(n)
空间复杂度是O(1)
'''
# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         '''nums中[0...k)中'''
#         k = 0
#         for i in range(0,len(nums)):
#             if nums[i] != 0:
#                 nums[k] = nums[i]
#                 k+=1
#         for i in range(k,len(nums)):
#             nums[i] = 0

'''
时间复杂度是O(s)，s为非0的个数，而不再是n
空间复杂度是O(1)
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''nums中[0...k)中'''
        k = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                '''k==i的时候，不需要自身交换'''
                if i != k:
                    nums[k],nums[i] = nums[i],nums[k]
                k+=1




sol = Solution()
arr = [1,2,3,4,5]
sol.moveZeroes(arr)
print(arr)