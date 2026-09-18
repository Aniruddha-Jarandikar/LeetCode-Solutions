class Solution:
    def isRectangleOverlap(self, rec1, rec2):

        # Check horizontal overlap
        horizontal = min(rec1[2], rec2[2]) > max(rec1[0], rec2[0])

        # Check vertical overlap
        vertical = min(rec1[3], rec2[3]) > max(rec1[1], rec2[1])

        return horizontal and vertical