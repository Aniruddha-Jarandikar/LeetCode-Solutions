class Solution:
    def totalNQueens(self, n):
        cols = set()
        diagonals1 = set()
        diagonals2 = set()

        def backtrack(row):
            if row == n:
                return 1

            count = 0

            for col in range(n):
                if (col in cols or
                    row - col in diagonals1 or
                    row + col in diagonals2):
                    continue

                cols.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)

                count += backtrack(row + 1)

                cols.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)

            return count

        return backtrack(0)