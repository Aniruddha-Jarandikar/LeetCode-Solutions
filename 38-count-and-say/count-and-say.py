class Solution:
    def countAndSay(self, n):

        result = "1"

        for _ in range(n - 1):

            new_result = ""
            i = 0

            while i < len(result):

                count = 1

                # Count consecutive same digits
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    count += 1
                    i += 1

                # Add count + digit
                new_result += str(count) + result[i]

                i += 1

            result = new_result

        return result