class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index = 1

        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                nums[index] = nums[i+1]
                index+=1

        return index

        
solution = Solution()
print(solution.removeDuplicates([1,1,2]))
print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))