# coding = utf-8
'''leetcode 167'''

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i,j = 0,len(numbers)-1
        arr = []
        while i < j:
            if numbers[i] + numbers[j] == target:
                arr.append(i+1)
                arr.append(j+1)
                return arr
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        return arr

    # def twoSum(self, numbers, target):
    #     """
    #     :type numbers: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     '''遍历i，在（i...]利用二分查找，target-nums[i]的值，时间复杂度是nlogn'''
    #     for i in range(len(numbers)):
    #         add = target-numbers[i]
    #         result = self.binarySearch(numbers[i:],add)
    #         if result:
    #             return [i+1,i+result+1]
    #         else:
    #             continue
    #     return []
    #
    #
    # def binarySearch(self,numbers,target):
    #     l,r = 1,len(numbers)-1
    #     while l<=r:
    #         mid = l + (r - l) // 2
    #         if target < numbers[mid]:
    #             r = mid-1
    #         elif target > numbers[mid]:
    #             l = mid+1
    #         else:
    #             return mid
    #     return False



sol = Solution()
arr = [2,7,9,11]
p = sol.twoSum(arr,15)
print(p)