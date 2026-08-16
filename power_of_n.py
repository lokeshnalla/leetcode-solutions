class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x=1/x
            n=-n
        val=1
        while n>0:
            if n%2==1:
                val=val*x
            x=x*x
            n=n//2
        return val

