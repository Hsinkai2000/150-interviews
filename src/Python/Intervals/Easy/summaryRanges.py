class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        start = "/"
        final = []
        for i in range (len(nums)):
            if i == len(nums)-1:
                if isinstance(start, int):
                    final.append(str(nums[start])+"->"+str(nums[i]))
                else:
                    final.append(str(nums[i]))   
            else:
                if nums[i] + 1 == nums[i+1]:
                    if not isinstance(start,int):
                        start = i
                else:
                    if isinstance(start, int):
                        final.append(str(nums[start])+"->"+str(nums[i]))
                        start = "/"
                    else:
                        final.append(str(nums[i]))    
            
        return final

s = Solution()
print(s.summaryRanges([0,1,2,4,5,7]))
print(s.summaryRanges([0,2,3,4,6,8,9]))