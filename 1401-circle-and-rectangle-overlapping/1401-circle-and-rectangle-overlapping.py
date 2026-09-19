class Solution:
    def checkOverlap(self, r, xC, yC, x1, y1, x2, y2):
        if xC < x1:
            x = x1
        elif xC > x2:
            x = x2
        else:
            x = xC

        if yC < y1:
            y = y1
        elif yC > y2:
            y = y2
        else:
            y = yC

        return (x-xC)**2 + (y-yC)**2 <= r**2