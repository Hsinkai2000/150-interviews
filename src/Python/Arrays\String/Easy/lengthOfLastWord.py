class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Calculates the length of the last word in a given string.

        Parameters:
        s (str): The input string.

        Returns:
        int: The length of the last word.
        """
        newString = s.split()
        return len(newString[-1])


solution = Solution()
print(solution.lengthOfLastWord("Hello World"))
print(solution.lengthOfLastWord("   fly me   to   the moon  "))
print(solution.lengthOfLastWord("luffy is still joyboy"))
