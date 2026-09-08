class Solution:
    def countCommas(self, n: int) -> int:
        c=0
        if n<1000:
            return 0
        else:
            c=c+(n-1000)+1
        return c
        