class Solution:
    def minMoves(self, nums: List[int]) -> int:
        a=max(nums)
        res=0
        for i in nums:
            res+=a-i
        return res