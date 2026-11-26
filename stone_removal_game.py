class Solution:
    def canAliceWin(self, n: int) -> bool:
        b=10
        a=False
        while n>=b:
            if b%2==0:
                a= True
            else:
                a=False
            n=n-b
            b-=1
        return a
        