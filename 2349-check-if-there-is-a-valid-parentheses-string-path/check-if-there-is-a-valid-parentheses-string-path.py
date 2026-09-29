class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Total characters in any path
        length = m + n - 1

        # A valid parentheses string must have even length
        if length % 2 == 1:
            return False

        # dp[i][j] = set of possible balances at (i, j)
        dp = [[set() for _ in range(n)] for _ in range(m)]

        # Starting cell must be '('
        if grid[0][0] == ')':
            return False

        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                # Get possible balances from top and left
                possible = set()

                if i > 0:
                    possible.update(dp[i - 1][j])

                if j > 0:
                    possible.update(dp[i][j - 1])

                # Calculate new balance
                for balance in possible:
                    if grid[i][j] == '(':
                        new_balance = balance + 1
                    else:
                        new_balance = balance - 1

                    # Balance can never be negative
                    if new_balance >= 0:
                        dp[i][j].add(new_balance)

        return 0 in dp[m - 1][n - 1]