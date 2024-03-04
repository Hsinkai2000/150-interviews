class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determines whether the input string `s` contains a valid arrangement of parentheses, curly brackets, and square brackets.

        Args:
            s (str): The input string to be checked.

        Returns:
            bool: True if the string is valid, False otherwise.
        """
        params = {"(": ")", "{": "}", "[": "]"}
        stack = []

        # If odd length
        if len(s) % 2 != 0:
            return False

        for c in s:
            if len(stack) == 0 and not c in params.keys():
                return False

            if len(stack) != 0 and c in params.values():
                if c == params[stack[-1]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if len(stack) == 0:
            return True
        return False

        




s = Solution()
print(s.isValid("()"))
print(s.isValid("({)}"))
print(s.isValid("({[)"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([}}])"))