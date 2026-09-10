class Solution:
    def minElement(self, nums: List[int]) -> int:
        res=0
        ans=[]
        for i in range(len(nums)):
            s=0
            a=nums[i]
            while a>0:
                
                b=a%10
                s=s+b
                a=a//10
            ans.append(s)
        return min(ans)
        