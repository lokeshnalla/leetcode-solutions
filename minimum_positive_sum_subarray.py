class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums)
        ans=float('inf')
        for i in range(n):
            total=0
            for j in range(i,n):
                total+=nums[j]
                if l<=j-i+1<=r and total>0:
                    ans=min(ans,total)
        if ans==float('inf'):
            return -1
        else:
            return ans
                    

        