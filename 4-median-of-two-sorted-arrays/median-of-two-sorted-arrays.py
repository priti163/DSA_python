class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
       return median(sorted(nums1 + nums2))
        