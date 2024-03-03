class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """
        Determines whether there are two distinct indices i and j in the given list of integers nums, 
        such that the absolute difference between nums[i] and nums[j] is at most k.

        Args:
            nums (list[int]): The list of integers.
            k (int): The maximum absolute difference between indices.

        Returns:
            bool: True if there are two distinct indices i and j satisfying the condition, False otherwise.
        """
        numSet = set()
        for i in range(len(nums)):
            if nums[i] in numSet:
                return True
            numSet.add(nums[i])
            if len(numSet) > k:
                numSet.remove(nums[i - k])
        return False

s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1],3))
print(s.containsNearbyDuplicate([1,0,1,1],1))
print(s.containsNearbyDuplicate([1,2,3,1,2,3],2))