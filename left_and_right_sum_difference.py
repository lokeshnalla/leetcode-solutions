class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans=[]
        left=[]
        right=[]
        if len(nums)<=1:
            return [0]
        add=0
        for i in range(len(nums)):
            left.append(add)
            add=add+nums[i]
        # add=add+nums[-1]
        for i in range(len(nums)):
            add=add-nums[i]
            right.append(add)
        # return right
        for i in range(len(nums)):
            ans.append(max(left[i],right[i])-min(left[i],right[i]))
        return ans
        
        