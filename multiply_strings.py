class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        res=[0]*(len(num1)+len(num2))
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                a=ord(num1[i])-ord("0")
                b=ord(num2[j])-ord("0")
                product=a*b
                pos1=i+j
                pos2=i+j+1
                total=product+res[pos2]
                res[pos2]=total%10
                res[pos1]+=total//10
        while(res[0]==0):
            res.pop(0)
        return "".join(str(i) for i in res)

        

        