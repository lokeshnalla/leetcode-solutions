# Problem: Two Sum II - Input Array is Sorted
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Approach: Two pointers

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        sum=0
        while l<r:
            sum=numbers[l]+numbers[r]
            if(sum==target):
                return [l+1,r+1]
            if(sum<target):
                l=l+1
            else:
                r=r-1
        return []