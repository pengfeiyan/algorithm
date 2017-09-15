'''lintcode 135'''
import collections
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    ret = []
    def combinationSum(self, candidates, target):
        # write your code here
        candidates.sort()
        self.findCombination(candidates,target,[])
        return self.ret

    def findCombination(self,candidates,target,arr):
        for i in candidates:
            nums = [x for x in arr]
            if i < target:
                nums.append(i)
                self.findCombination(candidates,target-i,nums)
            if i == target:
                nums.append(i)
                nums.sort()
                if nums not in self.ret:
                    self.ret.append(nums)
                return
            else:
                continue
        return




sol = Solution()
arr = [8,7,4,3]
print(sol.combinationSum(arr,11))