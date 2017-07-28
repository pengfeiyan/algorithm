'''leetcode 149 查找表'''
from decimal import *
import collections,time
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        count = 0

        for i in range(len(points)):
            res = self.line(i,points)
            if res > count:
                count = res
        print(count)

    def line(self,i,points):
        dic = {}
        same = 1
        for p in range(len(points)):
            if p!=i:
                if points[i].x-points[p].x != 0:
                    #k = self.div((points[i].x-points[p].x),(points[i].y-points[p].y))
                    dy = points[i].y-points[p].y
                    dx = points[i].x-points[p].x
                    k = Decimal(dy)/Decimal(dx)
                    if k not in dic:
                        dic[k] = 1
                    else:
                        dic[k] += 1
                elif points[i].x == points[p].x and points[i].y == points[p].y:
                    same += 1

                elif points[i].x == points[p].x:
                    k = 'wuqiong'
                    if k not in dic:
                        dic[k] = 1
                    else:
                        dic[k] += 1

        if dic.values():
            return max(dic.values())+same
        else:
            return same
    def div(self,a,b):
        if abs(a+b) == abs(a)+abs(b):
            flag = 1
        else:
            flag = -1
        quotient = a // b
        remainder = a % b
        if remainder == 0:
            return quotient
        ans = str(quotient) + '.'
        i = 0
        while i < 16:
            a = remainder * 10
            quotient = a // b
            remainder = a % b
            ans += str(quotient)
            if remainder == 0:
                break
            i += 1
        if flag == -1:
            ans = '-'+ans
        return ans

arr = [[0,0],[94911151,94911150],[94911152,94911151]]
p = [Point(x[0],x[1]) for x in arr]
sol = Solution()
start = time.time()
for i in range(1000):
    sol.maxPoints(p)

print(float(time.time()-start)/1000)


