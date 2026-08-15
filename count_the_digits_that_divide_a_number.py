class Solution:
    def countDigits(self, num: int) -> int:
        a=num
        c=0
        while num:
            if a%(num%10)==0:
                c=c+1
            num=num//10
        return c
        