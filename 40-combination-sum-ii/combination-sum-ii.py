class Solution:
    def combinationSum2(self, candidates, target):

        result = []

        candidates.sort()

        def backtrack(start, remaining, path):

            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):

                # Skip duplicate combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted
                if candidates[i] > remaining:
                    break

                # Choose the number
                path.append(candidates[i])

                # i + 1 because each number can be used only once
                backtrack(i + 1, remaining - candidates[i], path)

                # Undo
                path.pop()

        backtrack(0, target, [])

        return result