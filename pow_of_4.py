class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        a=1
        if n==1:
            return True
        for i in range(32):
            a=4*a
            if n==a:
                return True
                break
        return False
        