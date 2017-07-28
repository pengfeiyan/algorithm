# coding = utf-8
'''归并排序的应用'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = m
        while len(nums1) > m:
            nums1.pop()
        while len(nums2) > n:
            nums2.pop()
        nums1.extend(nums2)
        arr = [ x for x in nums1]
        for k in range(0,m+n):
            if i >= m:
                nums1[k] = arr[j]
                j += 1
            elif j >= n+m:
                nums1[k] = arr[i]
                i += 1
            elif arr[i] > arr[j]:
                nums1[k] = arr[j]
                j += 1
            else:
                nums1[k] = arr[i]
                i += 1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
sol = Solution()
sol.merge(nums1,3,nums2,3)
print(nums1)