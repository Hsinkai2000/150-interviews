from collections import Counter

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        """
        Finds the length of the longest consecutive subsequence in the given list of integers.

        Args:
            nums (list[int]): The list of integers.

        Returns:
            int: The length of the longest consecutive subsequence.

        """

        # if not nums:
        #     return 0
        # numsCounter = Counter(nums)
        # numsCounter = sorted(numsCounter.items())
        # current = numsCounter[0][0]
        # currCount = 1
        # count = 1
        # for i in range (1, len(numsCounter)):
        #     numi = numsCounter[i][0]
        #     if numi - 1 == current:
        #         count +=1
        #     else:
        #         count = 1            
        #     current = numi
        #     if currCount < count:
        #         currCount = count
        # return currCount
    
        if not nums:
            return 0
        numSet = set(nums)
        numSet = sorted(numSet)
        current = numSet[0]
        currCount = 1
        count = 1

        for i in range (1, len(numSet)):
            numi = numSet[i]
            if numi - 1 == current:
                count +=1
            else:
                count = 1            
            current = numi
            if currCount < count:
                currCount = count
        return currCount

    
s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(s.longestConsecutive([1,2,0,1]))
print(s.longestConsecutive([0]))
print(s.longestConsecutive([0,0]))
print(s.longestConsecutive([]))