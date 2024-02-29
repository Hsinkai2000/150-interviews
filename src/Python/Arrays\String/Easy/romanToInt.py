class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Converts a Roman numeral string to an integer.

        Args:
            s (str): The Roman numeral string to convert.

        Returns:
            int: The integer representation of the Roman numeral.

        """
        romanDict = {"i": 1,
                     "v": 5,
                     "x": 10,
                     "l": 50,
                     "c": 100,
                     "d": 500,
                     "m": 1000}

        s = s.lower()
        total = 0

        s = s.replace("iv", "iiii").replace("ix", "viiii").replace("xl", "xxxx").replace(
            "xc", "lxxxx").replace("cd", "cccc").replace("cm", "dcccc")

        for i in s:
            total += romanDict.get(i)

        return total


solution = Solution()
print(solution.romanToInt("III"))
print(solution.romanToInt("LVIII"))
