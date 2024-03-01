class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Determines if two strings, s and t, are isomorphic.

        Args:
            s (str): The first string.
            t (str): The second string.

        Returns:
            bool: True if the strings are isomorphic, False otherwise.
        """
        sDict = {}
        tDict = {}

        for s1, t1 in zip(s, t):
            if (s1 in sDict and sDict.get(s1) != t1) or (t1 in tDict and tDict.get(t1) != s1):
                return False
            sDict[s1] = t1
            tDict[t1] = s1
        return True


s = Solution()
print(s.isIsomorphic("egg", "add"))
print(s.isIsomorphic("foo", "bar"))
print(s.isIsomorphic("paper", "title"))
print(s.isIsomorphic("badc", "baba"))
