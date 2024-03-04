class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        """
        Returns a list of strings representing the summary ranges of the input list of integers.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            list[str]: A list of strings representing the summary ranges.

        Example:
            >>> nums = [0, 1, 2, 4, 5, 7]
            >>> summaryRanges(nums)
            ['0->2', '4->5', '7']
        """
        start = "/"
        final = []
        for i in range(len(nums)):
            if i == len(nums) - 1:
                if isinstance(start, int):
                    final.append(str(nums[start]) + "->" + str(nums[i]))
                else:
                    final.append(str(nums[i]))
            else:
                if nums[i] + 1 == nums[i + 1]:
                    if not isinstance(start, int):
                        start = i
                else:
                    if isinstance(start, int):
                        final.append(str(nums[start]) + "->" + str(nums[i]))
                        start = "/"
                    else:
                        final.append(str(nums[i]))

        return final

s = Solution()
print(s.summaryRanges([0,1,2,4,5,7]))
print(s.summaryRanges([0,2,3,4,6,8,9]))