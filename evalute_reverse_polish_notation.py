class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for i in tokens:
            if i=="+":
                a=s.pop()
                s[-1]=s[-1]+a
            elif i=="-":
                a=s.pop()
                s[-1]=s[-1]-a
            elif i=="/":
                a=s.pop()
                if a==0:
                    s[-1]=0
                else:
                    s[-1]=int(s[-1]/a)
            elif i=="*":
                a=s.pop()
                s[-1]=s[-1]*a
            else:
                s.append(int(i))
        return s[0]
        