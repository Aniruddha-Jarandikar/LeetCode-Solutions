class Solution:
    def isMatch(self, s, p):

        i = 0
        j = 0

        star = -1
        match = 0

        while i < len(s):

            # Characters match or '?' matches any character
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1

            # Found '*'
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1

            # Previous '*' can match this character
            elif star != -1:
                j = star + 1
                match += 1
                i = match

            # No match possible
            else:
                return False

        # Remaining pattern must contain only '*'
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)