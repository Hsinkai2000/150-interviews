class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Merges two sorted arrays, nums1 and nums2, into nums1 in non-decreasing order.

        Args:
            nums1 (list[int]): The first sorted array.
            m (int): The number of elements in nums1 (excluding the extra space).
            nums2 (list[int]): The second sorted array.
            n (int): The number of elements in nums2.

        Returns:
            None
        """

        tracker = m + n - 1
        m -= 1
        n -= 1

        while n >= 0:
            if nums1[m] >= nums2[n] and m >= 0:
                nums1[tracker] = nums1[m]
                m -= 1
            else:
                nums1[tracker] = nums2[n]
                n -= 1
            tracker -= 1

        print(nums1)


solution = Solution()
solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
solution.merge([2, 0], 1, [1], 1)
