class Solution:
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):

        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))

        distanceSquared = (closestX - xCenter) ** 2 + (closestY - yCenter) ** 2

        return distanceSquared <= radius ** 2