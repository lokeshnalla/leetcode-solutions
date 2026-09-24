class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        num=[0]*len(nums)
        for i in range(len(nums)):
            sums=0
            if nums[i]>9:
                a=nums[i]
                while(a>0):
                    sums+=a%10
                    a=a//10
            else:
                sums=nums[i]
            num[i]=sums
            if num[i]==i:
                return i
                break
        return -1
        