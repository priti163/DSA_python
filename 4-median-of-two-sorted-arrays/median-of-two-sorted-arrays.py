class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        # Always binary search on the smaller array
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        low = 0
        high = n1

        total = n1 + n2
        left = (total + 1) // 2

        while low <= high:

            mid1 = (low + high) // 2
            mid2 = left - mid1

            # Boundary values
            l1 = float('-inf')
            l2 = float('-inf')
            r1 = float('inf')
            r2 = float('inf')

            if mid1 < n1:
                r1 = nums1[mid1]

            if mid2 < n2:
                r2 = nums2[mid2]

            if mid1 > 0:
                l1 = nums1[mid1 - 1]

            if mid2 > 0:
                l2 = nums2[mid2 - 1]

            # Correct partition
            if l1 <= r2 and l2 <= r1:

                # Odd number of elements
                if total % 2 == 1:
                    return float(max(l1, l2))

                # Even number of elements
                return (max(l1, l2) + min(r1, r2)) / 2.0

            # Too many elements taken from nums1
            elif l1 > r2:
                high = mid1 - 1

            # Too few elements taken from nums1
            else:
                low = mid1 + 1

        return 0.0

        