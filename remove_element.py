class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # 'c' represents the position where the next
        # valid element should be placed
        c = 0

        # Store the length of the array
        d = len(nums)

        # Traverse every element in the array
        for i in range(d):

            # If current element is NOT equal to val,
            # we want to keep it
            if nums[i] != val:

                # Place the valid element at index c
                nums[c] = nums[i]

                # Move c to the next available position
                c = c + 1

        # c represents the number of elements
        # that are not equal to val
        return c