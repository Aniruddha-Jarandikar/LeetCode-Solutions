class Solution:
    def solveNQueens(self, n):
        result = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        diagonals1 = set()   # row - col
        diagonals2 = set()   # row + col

        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):

                # Check whether queen can be placed
                if col in cols or (row - col) in diagonals1 or (row + col) in diagonals2:
                    continue

                # Place queen
                board[row][col] = "Q"
                cols.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)

                # Move to next row
                backtrack(row + 1)

                # Remove queen (backtrack)
                board[row][col] = "."
                cols.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)

        backtrack(0)

        return result