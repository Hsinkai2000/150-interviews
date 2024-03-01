class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        Finds the longest common prefix among a list of strings.

        Args:
            strs (list[str]): The list of strings to find the longest common prefix from.

        Returns:
            str: The longest common prefix among the strings.
        """
        # # Slow but working solution
        # index = 0
        # var = ""
        # currChar=""

        # if "" in strs: #check for ""
        #     return ""

        # while index < len(min(strs, key=len)):
        #     currChar = strs[0][index]
        #     for string in strs:
        #         if not string[index] == currChar:
        #             return var
        #     var += currChar
        #     index+=1
        #     if index == len(min(strs, key=len)):
        #         return var

        # input: ["flower","flow","flight"]

        # faster method
        result = ""
        strs = sorted(strs)  # ['flight', 'flow', 'flower']

        first = strs[0]
        last = strs[-1]

        for i in range(len(min(strs, key=len))):  # i from 0 to len of shortest string
            if not first[i] == last[i]:
                return result
            result += first[i]

        return result


s = Solution()
print(s.longestCommonPrefix(["", ""]))
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print(s.longestCommonPrefix(["flo", "flo", "flo", "flo"]))
print(s.longestCommonPrefix(["dog", "racecar", "car"]))
