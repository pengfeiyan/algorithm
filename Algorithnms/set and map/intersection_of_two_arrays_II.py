# coding=utf-8
import collections
'''leetcode 350'''

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counts1 = collections.Counter(nums1)
        counts2 = collections.Counter(nums2)
        return list((counts1&counts2).elements())


sol = Solution()
nums1 = [1,2,2,2,1]
nums2 = [2,2,1]
print(sol.intersect(nums1,nums2))
