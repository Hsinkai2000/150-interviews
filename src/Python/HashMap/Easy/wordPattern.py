class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Checks if a given pattern matches a string of words.

        Args:
            pattern (str): The pattern to match.
            s (str): The string of words to check.

        Returns:
            bool: True if the pattern matches the string of words, False otherwise.
        """
        s = s.split()
        if pattern == "" or len(s) != len(pattern):
            return False
        
        wordDict = {}

        for i in range(len(s)):
            char = pattern[i]
            word = s[i]
            if (word in wordDict.values() and wordDict.get(char) != word) or (wordDict.get(char) != None and wordDict.get(char) != word):
                return False
            wordDict[char] = word

        return True
    
s = Solution()
print(s.wordPattern("abba","dog cat cat dog"))
print(s.wordPattern("abba","dog cat cat fish"))
print(s.wordPattern("aaaa","dog cat cat dog"))
print(s.wordPattern("aaa","dog cat cat dog"))