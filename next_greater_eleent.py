class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Stack stores numbers whose next greater
        # element has not been found yet
        stack = []

        # Store the next greater element of each number
        greater = {}

        # Process nums2 only once
        for num in nums2:

            # If current number is greater than the
            # top of stack, current number is the
            # next greater element of the top
            while stack and num > stack[-1]:

                smaller = stack.pop()

                greater[smaller] = num

            # Current number is now waiting for
            # its own next greater element
            stack.append(num)

        # Elements remaining in stack have no
        # greater element
        while stack:
            greater[stack.pop()] = -1

        # Find answers for nums1 using the dictionary
        ans = []

        for num in nums1:
            ans.append(greater[num])

        return ans