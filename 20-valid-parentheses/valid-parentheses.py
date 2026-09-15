class Solution:
    def isValid(self, s):
        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:

            # Opening bracket
            if char in "({[":
                stack.append(char)

            # Closing bracket
            else:
                if not stack or stack[-1] != pairs[char]:
                    return False

                stack.pop()

        return len(stack) == 0