class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        bol=[True]*n
        bol[0]=bol[1]=False
        for i in range(2,int(n**0.5)+1):
            if bol[i]:
                for j in range(i*i,n,i):
                    bol[j]=False
        return sum(bol)
        