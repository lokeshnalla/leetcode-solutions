class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        # Pointer to the last valid element in nums1
        a = m - 1

        # Pointer to the last element in nums2
        b = n - 1

        # Pointer to the last position of nums1 (including extra space)
        c = m + n - 1

        # Compare elements from the end of both arrays
        while a >= 0 and b >= 0:

            # If nums2 has the larger element,
            # place it at the end of nums1
            if nums1[a] <= nums2[b]:
                nums1[c] = nums2[b]
                b -= 1

            # Otherwise, place nums1's element
            else:
                nums1[c] = nums1[a]
                a -= 1

            # Move to the next position from the end
            c -= 1

        # If nums2 still has remaining elements,
        # copy them into nums1
        while b >= 0:
            nums1[c] = nums2[b]
            b -= 1
            c -= 1

        # No need to copy remaining elements of nums1
        # because they are already in the correct position.