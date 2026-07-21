class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]):

        # Pointers for nums1 and nums2
        left = 0
        right = 0

        # Total number of elements
        a = len(nums1) + len(nums2)

        # Merged array
        l = []

        # Merge both arrays until one of them is exhausted
        while left < len(nums1) and right < len(nums2):

            # Add the smaller element
            if nums1[left] < nums2[right]:
                l.append(nums1[left])
                left += 1
            else:
                l.append(nums2[right])
                right += 1

        # Add remaining elements from nums1
        while left < len(nums1):
            l.append(nums1[left])
            left += 1

        # Add remaining elements from nums2
        while right < len(nums2):
            l.append(nums2[right])
            right += 1

        # If total length is odd
        if a % 2 == 1:
            return l[a // 2]

        # If total length is even
        else:
            return (l[a // 2] + l[a // 2 - 1]) / 2