'''leetcode 49 查找表'''

class Solution(object):
    def groupAnagrams(self, strs):
        d = {}
        ans = []
        k = 0
        for str in strs:
            sstr = ''.join(sorted(str))
            if sstr not in d:
                '''将这个单词记录在字典中，key是排序过后的单词，value是ans的下标'''
                d[sstr] = k
                k = k+1
                ans.append([str])
                #ans[-1].append(str)
            else:
                '''排序后发现在字段中存在，就找出value，ans[value]就是相同单词的列表，填入即可'''
                ans[d[sstr]].append(str)
        print(ans)

sol = Solution()
arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
# for i in sol.groupAnagrams(arr):
#     print(i)

sol.groupAnagrams(arr)

