class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0

        for i in range (len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index+=1

        return index

        
solution = Solution()
print(solution.removeElement([3,2,2,3],3))
print(solution.removeElement([0,1,2,2,3,0,4,2],2))

print(solution.removeElement([2],2))