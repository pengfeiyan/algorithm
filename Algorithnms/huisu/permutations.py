'''leetcode 46'''

class Solution(object):
    ret = []
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return self.ret
        self.perm(nums,0,[])
        return self.ret

    def perm(self,nums,index,p):
        arr = [x for x in p]
        if index == len(nums):
            self.ret.append(arr)
            return
        for i in nums:
            if i not in arr:
                arr.append(i)
                self.perm(nums,index+1,arr)
        return