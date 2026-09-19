class Solution:
    def maximumScore(self, grid):

        n = len(grid)

        # Prefix sums for every column
        prefix = [[0] * (n + 1) for _ in range(n)]

        for j in range(n):
            for i in range(n):
                prefix[j][i + 1] = prefix[j][i] + grid[i][j]

        # Sum of grid[j] from row l to r-1
        def get_sum(j, l, r):
            if r <= l:
                return 0
            return prefix[j][r] - prefix[j][l]

        NEG = -10**30

        # dp[a][b]
        # a = height of previous column
        # b = height of current column
        dp = [[NEG] * (n + 1) for _ in range(n + 1)]

        # Left boundary has height 0
        for h in range(n + 1):
            dp[0][h] = 0

        # Process columns 0 ... n-2
        for j in range(n - 1):

            new_dp = [[NEG] * (n + 1) for _ in range(n + 1)]

            for b in range(n + 1):

                # suffix[a] =
                # max(dp[a][b] + contribution when a >= c)
                suffix = [NEG] * (n + 2)

                for a in range(n, -1, -1):

                    value = dp[a][b]

                    if value != NEG:
                        value += get_sum(j, b, a)

                    suffix[a] = max(suffix[a + 1], value)

                # prefix maximum of dp[a][b]
                prefix_max = [NEG] * (n + 1)
                best = NEG

                for a in range(n + 1):
                    best = max(best, dp[a][b])
                    prefix_max[a] = best

                for c in range(n + 1):

                    # Case 1:
                    # a >= c
                    # max(a,c) = a
                    best_value = suffix[c]

                    # Case 2:
                    # a < c
                    # max(a,c) = c
                    if c > 0:
                        best_value = max(
                            best_value,
                            prefix_max[c - 1] + get_sum(j, b, c)
                        )

                    new_dp[b][c] = best_value

            dp = new_dp

        # Right boundary has height 0
        answer = 0

        for a in range(n + 1):
            for b in range(n + 1):

                if dp[a][b] != NEG:
                    answer = max(
                        answer,
                        dp[a][b] + get_sum(n - 1, b, a)
                    )

        return answer