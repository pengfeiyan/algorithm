# coding=utf-8
import random
''' leetcode 75 计数排序'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # arr = [0,0,0]
        # for i in range(len(nums)):
        #     arr[nums[i]] += 1
        # for index in range(arr[0]):
        #     nums[index] = 0
        #     index += 1
        # for index in range(arr[1]):
        #     nums[index+arr[0]] = 1
        #     index += 1
        # for index in range(arr[2]):
        #     nums[index+arr[0]+arr[1]] = 2
        #     index += 1

        zero = -1
        two = len(nums)
        i = 0
        while i < two:
            if nums[i] == 1:
                i+=1
            elif nums[i] == 2:
                nums[i],nums[two-1] = nums[two-1],nums[i]
                two -= 1
            elif nums[i] == 0:
                nums[zero+1],nums[i] = nums[i],nums[zero+1]
                i+=1
                zero += 1

arr = [random.randint(0,2) for x in range(10)]

sol = Solution()
sol.sortColors(arr)
print("后：",arr)
