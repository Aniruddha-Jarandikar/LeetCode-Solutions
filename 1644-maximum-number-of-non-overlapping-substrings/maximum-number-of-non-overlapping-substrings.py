class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)
        first, last = {}, {}
        for i in range(n):
            ch = s[i]
            if ch not in first:
                first[ch] = i
            last[ch] = i

        def build(c):
            """Minimal valid interval containing all occurrences of c,
               or None if it's subsumed by another character's interval."""
            left, right = first[c], last[c]
            i = left
            while i <= right:
                ch = s[i]
                if first[ch] < left:
                    return None
                if last[ch] > right:
                    right = last[ch]
                i += 1
            return (left, right)

        intervals = []
        for c in first:
            iv = build(c)
            if iv is not None:
                intervals.append(iv)

        # earliest ending first; for equal ends, the shorter one first
        intervals.sort(key=lambda p: (p[1], p[1] - p[0]))

        res = []
        prev_end = -1
        for left, right in intervals:
            if left > prev_end:
                res.append(s[left:right + 1])
                prev_end = right
        return res