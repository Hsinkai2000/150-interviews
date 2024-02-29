class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # #Working but slow solution
        # if needle in haystack:
        #     return haystack.index(needle)
        # return -1

        #faster solution
        needleL = len(needle)
        haystackL = len(haystack)
        if needleL > haystackL: return -1
        
        for i in range(haystackL-needleL+1):
            if haystack[i:i+needleL] == needle:
                return i
        
        return -1


s = Solution()
print(s.strStr("sadbutsad","sad"))
print(s.strStr("leetcode", "leeto")) #8 , 5