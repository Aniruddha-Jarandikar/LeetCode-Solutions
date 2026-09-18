class Solution:
    def maxPalindromes(self, s, k):
        n = len(s)

        # palindrome[i][j] = True if s[i:j+1] is a palindrome
        palindrome = [[False] * n for _ in range(n)]

        # Every single character is a palindrome
        for i in range(n):
            palindrome[i][i] = True

        # Check substrings of length 2 or more
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                if s[left] == s[right]:
                    if length == 2 or palindrome[left + 1][right - 1]:
                        palindrome[left][right] = True

        # dp[i] = maximum number of palindromes
        # using the first i characters
        dp = [0] * (n + 1)

        for right in range(n):
            # Don't use a substring ending at right
            dp[right + 1] = dp[right]

            # Try every possible starting position
            for left in range(right + 1):
                length = right - left + 1

                if length >= k and palindrome[left][right]:
                    dp[right + 1] = max(
                        dp[right + 1],
                        dp[left] + 1
                    )

        return dp[n]