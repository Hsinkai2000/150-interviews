from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determines whether two strings are anagrams of each other.

        Args:
            s (str): The first string.
            t (str): The second string.

        Returns:
            bool: True if the strings are anagrams, False otherwise.
        """

        # Without using Counter but slower
        # if len(t) != len(s): return False

        # sDict, tDict = {}, {}

        # for i in range (len (t)):
        #     sword = s[i] 
        #     tword = t[i]
        #     sDict[sword] = sDict.get(sword, 1) + 1
        #     tDict[tword] = tDict.get(tword, 1) + 1
        
        # sorted(sDict.items())
        # sorted(tDict.items())

        # if sDict != tDict: return False

        # return True


        # Using Counter but faster
        if len(t) != len(s): return False
        sCounter, tCounter = Counter(s), Counter(t)
        if sCounter != tCounter: return False

        return True


s = Solution()
print(s.isAnagram("anagram","nagaram"))
print (s.isAnagram("rat","car"))
print(s.isAnagram("", " "))
print(s.isAnagram("aacc", "ccac"))