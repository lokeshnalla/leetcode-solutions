class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        arr=[]
        depth=0
        for i in seq:
            if i=="(":
                depth+=1
                arr.append(depth%2)
            else:
                arr.append(depth%2)
                depth-=1
        return arr
        