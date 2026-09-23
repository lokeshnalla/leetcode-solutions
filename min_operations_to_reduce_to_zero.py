class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        sum1=sum(nums)
        a=len(nums)
        target=sum1-x
        maxi=-1
        curr=0
        left=0
        for i in range(a):
            curr=curr+nums[i]
            while curr>target and left<=i:
                curr=curr-nums[left]
                left+=1
            if curr==target:
                maxi=max(maxi,i-left+1)
        if maxi==-1:
            return -1
        return a-maxi
        