class Solution:
    def multiply(self, num1, num2):

        if num1 == "0" or num2 == "0":
            return "0"

        n = len(num1)
        m = len(num2)

        result = [0] * (n + m)

        for i in range(n - 1, -1, -1):

            for j in range(m - 1, -1, -1):

                product = int(num1[i]) * int(num2[j])

                pos1 = i + j
                pos2 = i + j + 1

                total = product + result[pos2]

                result[pos2] = total % 10
                result[pos1] += total // 10

        # Remove leading zeros
        result = ''.join(map(str, result)).lstrip('0')

        return result