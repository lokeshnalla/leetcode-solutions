class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index=1
        occur=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                occur+=1
            else:
                occur=1
            if occur<=2:
                nums[index]=nums[i]
                index+=1
        return index