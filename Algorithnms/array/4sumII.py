'''leetcode 454'''
import collections
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        record = collections.Counter()
        for i in C:
            for j in D:
                record[i+j] += 1
        count = 0
        for m in A:
            for n in B:
                search = 0-m-n
                if record[search]:
                    count += record[search]
        print(count)


sol = Solution()
A = [1,2]
B = [-2,-1]
C = [-1,2]
D = [0,2]
sol.fourSumCount(A,B,C,D)