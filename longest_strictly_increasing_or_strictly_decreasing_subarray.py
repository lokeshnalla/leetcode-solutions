class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans=1
        n=len(nums)
        max1=1
        max2=1
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                max1+=1
                max2=1
            elif nums[i]<nums[i-1]:
                max1=1
                max2+=1
            else:
                max1=1
                max2=1
            ans=max(ans,max1,max2)
        return ans

        