class Solution:
    def resultArray(self, nums, k):
        dp = [0] * k
        result = [0] * k

        for num in nums:
            rem = num % k
            new_dp = [0] * k

            # Subarray containing only the current element
            new_dp[rem] += 1

            # Extend previous subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_rem = (r * rem) % k
                    new_dp[new_rem] += dp[r]

            dp = new_dp

            # Add subarrays ending at current position
            for r in range(k):
                result[r] += dp[r]

        return result