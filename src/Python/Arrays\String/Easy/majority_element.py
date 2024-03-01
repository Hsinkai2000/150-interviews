class Solution:
    """
    Class representing a solution for finding the majority element in a list of integers.
    """

    def majorityElement(self, nums: list[int]) -> int:
        """
        Finds the majority element in the given list of integers.

        Args:
            nums (list[int]): The list of integers.

        Returns:
            int: The majority element.

        """
        majorityNum = len(nums)/2
        m = dict()

        for num in nums:
            if (num in m):
                m[num] = m[num] + 1
            else:
                m[num] = 1
        highestkey = 0
        highestvalue = 0
        for key in m:
            if (m[key] > highestvalue):
                highestvalue = m[key]
                highestkey = key

        return highestkey


solution = Solution()
print(solution.majorityElement([3, 2, 3]))
