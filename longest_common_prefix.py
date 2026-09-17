class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre=strs[0]
        for i in strs[1:]:
            j=0
            while j<len(pre) and j<len(i):
                if pre[j] != i[j]:
                    break
                j=j+1
            pre=pre[:j]
        return pre


        
        