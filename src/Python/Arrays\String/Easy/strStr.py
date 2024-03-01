class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Returns the index of the first occurrence of the needle string in the haystack string.
        If the needle is not found in the haystack, returns -1.

        Parameters:
        - haystack (str): The string to search in.
        - needle (str): The string to search for.

        Returns:
        - int: The index of the first occurrence of the needle in the haystack, or -1 if not found.
        """

        needleL = len(needle)
        haystackL = len(haystack)
        if needleL > haystackL:
            return -1

        for i in range(haystackL-needleL+1):
            if haystack[i:i+needleL] == needle:
                return i

        return -1


s = Solution()
print(s.strStr("sadbutsad", "sad"))
print(s.strStr("leetcode", "leeto"))  # 8 , 5
