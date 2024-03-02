class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Finds two numbers in the given list that add up to the target value.

        Args:
            nums (list[int]): The list of integers.
            target (int): The target value.

        Returns:
            list[int]: A list containing the indices of the two numbers that add up to the target value.
        """        
        for i in range(len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,2,4], 6))
print(s.twoSum([3,3], 6))
print(s.twoSum([2,5,5,11],10))
print(s.twoSum([-1,-2,-3,-4,-5],-8))