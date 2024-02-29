class Solution:
    """
    Class representing a solution for checking if a string is a subsequence of another string.
    """

    def checkSubsequence(self, s:str, t:str) -> bool:
        """
        Checks if string s is a subsequence of string t.

        Args:
            s (str): The string to be checked as a subsequence.
            t (str): The string to be checked against.

        Returns:
            bool: True if s is a subsequence of t, False otherwise.
        """
        for j in range(len(t)):
            if t[j] == s[0]:
                if len(s) == 1:
                    return True
                else:
                    s=s[1:]
            elif j == len(t)-1:
                return False

    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Checks if string s is a subsequence of string t.

        Args:
            s (str): The string to be checked as a subsequence.
            t (str): The string to be checked against.

        Returns:
            bool: True if s is a subsequence of t, False otherwise.
        """
        if len(s) > 0:
            result = self.checkSubsequence(s,t)        
            return result
        return True

        
s = Solution()
print(s.isSubsequence("ab","baab"))
print(s.isSubsequence("abc","ahbgdc"))
print(s.isSubsequence("axc","ahbgdc"))