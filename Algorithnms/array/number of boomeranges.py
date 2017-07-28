'''leetcode 447 查找表'''
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        dict = {}
        res = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    distance = self.dis(points[i],points[j])
                    if distance in dict:
                        dict[distance] += 1
                    else:
                        dict[distance] = 1
            for k,v in dict.items():
                if v >= 2:
                    res += v*(v-1)
            dict.clear()
        print(res)

    def dis(self,pa,pb):
        return abs((pa[0]-pb[0])**2+(pa[1]-pb[1])**2)

sol = Solution()
arr = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
sol.numberOfBoomerangs(arr)
