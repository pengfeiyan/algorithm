'''lintcode 172'''

class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        # i为等于elem的位置，j为不等于elem的位置
        # i,j = 0,0
        # while j < len(A):
        #     if A[i] != elem and A[j] != elem:
        #         i += 1
        #         j += 1
        #     elif A[i] == elem and A[j] == elem:
        #         j += 1
        #     elif A[j] != elem:
        #         A[i],A[j] = A[j],A[i]
        #         i += 1
        #         j = i
        # return i

        k = 0
        for i in range(len(A)):
            if A[i] != elem:
                A[i],A[k] = A[k],A[i]

            k+= 1
        return k