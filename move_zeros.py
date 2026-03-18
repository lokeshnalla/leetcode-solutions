# Problem: Move Zeroes
# Link: https://leetcode.com/problems/move-zeroes/
# Approach: Shift non-zero elements forward

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        j=0
        for i in range(n):
            if(nums[i] !=0):
                nums[j]=nums[i]
                j=j+1
        for j in range(j,n):
            nums[j]=0