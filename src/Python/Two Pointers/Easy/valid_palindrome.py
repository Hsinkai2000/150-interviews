class Solution:
    """
    Class representing a solution for checking if a string is a palindrome.
    """

    def isPalindrome(self, s: str) -> bool:
        """
        Checks if the given string is a palindrome.

        Args:
            s (str): The input string to check.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        s = s.lower()
        rCount = len(s) - 1
        lCount = 0

        while lCount < rCount:
            if not s[lCount].isalnum():
                lCount += 1
            elif not s[rCount].isalnum():
                rCount -= 1
            elif s[lCount] != s[rCount]:
                return False
            else:
                lCount += 1
                rCount -= 1

        return True


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome(".,."))
print(solution.isPalindrome(" "))
