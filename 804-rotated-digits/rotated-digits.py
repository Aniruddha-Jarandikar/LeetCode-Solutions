class Solution:
    def rotatedDigits(self, n):
        good = 0

        for num in range(1, n + 1):
            s = str(num)

            # Invalid digits
            if any(d in "347" for d in s):
                continue

            # Must contain at least one digit that changes
            if any(d in "2569" for d in s):
                good += 1

        return good