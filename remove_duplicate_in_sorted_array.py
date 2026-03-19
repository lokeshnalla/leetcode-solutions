class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=len(nums)
        b=1
        if(a==0):
            return 0
        for i in range(1,a):
            if(nums[i] != nums[i-1]):
                nums[b]=nums[i]
                b=b+1
        return b
                