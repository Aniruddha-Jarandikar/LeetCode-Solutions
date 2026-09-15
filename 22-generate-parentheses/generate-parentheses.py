class Solution:
    def generateParenthesis(self, n):
        result = []

        def backtrack(current, open, close):

            # Complete valid combination
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add opening bracket
            if open < n:
                backtrack(current + "(", open + 1, close)

            # Add closing bracket
            if close < open:
                backtrack(current + ")", open, close + 1)

        backtrack("", 0, 0)

        return result