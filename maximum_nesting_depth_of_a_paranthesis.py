class Solution:
    def maxDepth(self, s: str) -> int:
        a=0
        c=0
        for i in s:
            if i=="(":
                c+=1
            if i==")":
                c-=1
            a=max(a,c)
        return a
        