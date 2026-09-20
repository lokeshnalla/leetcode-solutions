class Solution:
    def reverseDegree(self, s: str) -> int:
        sum1=0
        for i in range(len(s)):
            sum1+=(ord('z')-ord(s[i])+1)*(i+1)
        return sum1