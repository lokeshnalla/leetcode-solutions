class Solution:
    def checkString(self, s: str) -> bool:
        count=0
        for i in s:
            if i=='b':
                count+=1
            else:
                if count !=0:
                    return False
        return True