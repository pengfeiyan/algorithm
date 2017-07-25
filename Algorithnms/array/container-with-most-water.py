# coding=utf-8

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r = 0,len(height)-1
        ans = 0
        while l < r:
            v = (r-l)*min(height[l],height[r])
            if v > ans:ans = v
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        print(ans)

sol = Solution()
height = [1,2,10,1,1,2]
sol.maxArea(height)