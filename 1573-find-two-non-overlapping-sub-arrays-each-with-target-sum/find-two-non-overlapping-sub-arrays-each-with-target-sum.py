class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        INF = float('inf')
        best = [INF] * n

        left = 0
        curr_sum = 0
        min_length = INF
        answer = INF

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                # Combine with the best subarray before this one
                if left > 0 and best[left - 1] != INF:
                    answer = min(answer, length + best[left - 1])

                # Keep the shortest subarray ending here
                min_length = min(min_length, length)

            # Best subarray seen up to 'right'
            best[right] = min_length

        return -1 if answer == INF else answer