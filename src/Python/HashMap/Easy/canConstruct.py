from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Determines whether it is possible to construct the ransom note from the given magazine.

        Args:
            ransomNote (str): The ransom note string.
            magazine (str): The magazine string.

        Returns:
            bool: True if the ransom note can be constructed from the magazine, False otherwise.
        """

        # ransomDict = {}
        # magazineDict = {}
        # for letter in ransomNote:
        #     ransomDict[letter] = ransomDict.get(letter, 0) + 1

        # # Made it slow
        # for letter in magazine:
        #     if not ransomDict.get(letter) == None:
        #         ransomDict[letter] -= 1

        # if not ransomDict[max(ransomDict, key=ransomDict.get)] > 0:
        #     return True
        # return False

        magazineDict, ransomDict = Counter(magazine), Counter(ransomNote)

        return ransomDict & magazineDict == ransomDict


s = Solution()
print(s.canConstruct("a", "b"))
print(s.canConstruct("aa", "ab"))
print(s.canConstruct("aa", "aab"))
