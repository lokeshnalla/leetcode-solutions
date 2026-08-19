class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=[]
        nums1=nums1.sort()
        nums2=nums2.sort()
        l=0
        r=0
        while l<len(nums1) or r<len(nums2):
            if nums1[l]==nums2[r]:
                a.append(nums1[l])
                l=l+1
                r=r+1
            if nums1[l]<nums2[r]:
                l=l+1
            if nums1[l]>nums2[r]:
                r=r+1
        return a
            
    