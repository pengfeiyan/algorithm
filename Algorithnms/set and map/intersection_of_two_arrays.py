# coding=utf-8

'''leetcode 349'''

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # arr1 = list(set(nums1))
        # record = []
        # for i in nums2:
        #     if i in arr1:
        #         record.append(i)
        #
        # return list(set(record))

        return list(set(nums1)&set(nums2))


sol = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(sol.intersection(nums1,nums2))