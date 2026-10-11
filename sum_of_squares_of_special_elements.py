class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sums=0
        a=len(nums)
        for i in range(a):
            if a%(i+1)==0:
                sums=sums+nums[i]**2
        return sums