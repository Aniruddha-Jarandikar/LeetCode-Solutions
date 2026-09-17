class Solution:
    def getPermutation(self, n, k):
        numbers = list(range(1, n + 1))
        result = []

        k -= 1

        for i in range(n, 0, -1):
            factorial = 1

            for j in range(1, i):
                factorial *= j

            index = k // factorial
            k %= factorial

            result.append(str(numbers.pop(index)))

        return ''.join(result)