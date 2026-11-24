class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n=len(nums)
        ans=1
        for i in range(n):
            product=lc=hc=nums[i]
            for j in range(i+1,n):
                product*=nums[j]
                lc=lcm(lc,nums[j])
                hc=gcd(hc,nums[j])
                if product != lc*hc:
                    break    
                ans=max(ans,j-i+1)
        return ans

        