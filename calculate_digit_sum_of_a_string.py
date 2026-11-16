class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while(len(s)>k):
            new_str=''
            for i in range(0,len(s),k):
                group=s[i:i+k]
                total=0
                for j in group:
                    total+=int(j)
                new_str+=str(total)
            s=new_str        
        return s