class Solution:
    def distance(self, nums):

        positions = {}

        for i, num in enumerate(nums):
            if num not in positions:
                positions[num] = []
            positions[num].append(i)

        ans = [0] * len(nums)

        for indices in positions.values():

            total = sum(indices)
            prefix = 0

            for k, idx in enumerate(indices):

                left_count = k
                right_count = len(indices) - k - 1

                left_sum = prefix
                right_sum = total - prefix - idx

                left_distance = left_count * idx - left_sum
                right_distance = right_sum - right_count * idx

                ans[idx] = left_distance + right_distance

                prefix += idx

        return ans