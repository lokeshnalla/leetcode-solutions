class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=len(nums)
        sum1=a*(a+1)//2
        b=0
        for i in nums:
            b=b+i
        return sum1-b