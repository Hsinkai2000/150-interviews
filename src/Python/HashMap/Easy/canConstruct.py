from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
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
