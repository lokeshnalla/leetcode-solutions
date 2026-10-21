class Solution:
    def minOperations(self, s: str) -> int:
        if list(s)==sorted(s):
            return 0
        a=len(s)
        if a==2:
            return -1
        mn=min(s)
        mx=max(s)
        if mn==s[0] or mx==s[-1]:
            return 1
        if mn in s[1:-1] or mx in s[1:-1]:
            return 2
        return 3
