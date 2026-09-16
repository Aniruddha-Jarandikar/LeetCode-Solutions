class Solution:
    def divide(self, dividend, divisor):

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Special overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive values
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:

            current = divisor
            multiple = 1

            # Keep doubling while possible
            while dividend >= current + current:
                current += current
                multiple += multiple

            dividend -= current
            quotient += multiple

        if negative:
            quotient = -quotient

        return quotient