'''leetcode 17'''


class Solution(object):
    dic = {
        '1': " ",
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    ret = []
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.findCombination(digits,0,"")
        return self.ret
        # if not digits:
        #     return []
        # ret = [""]
        # for i in digits:
        #     tmp = []
        #     for k in dic[i]:
        #         for j in ret:
        #             tmp.append(j+k)
        #     ret = tmp
        # return ret

    def findCombination(self,digits,index,s):
        if index == len(digits):
            self.ret.append(s)
            return
        c = digits[index]
        letters = self.dic[c]
        for i in letters:
            self.findCombination(digits,index+1,s+i)
        return

sol = Solution()
print(sol.letterCombinations("234"))