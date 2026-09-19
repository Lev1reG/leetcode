class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if xCenter < x1:
            closestX = x1
        elif xCenter > x2:
            closestX = x2
        else:
            closestX = xCenter
        
        if yCenter < y1:
            closestY = y1
        elif yCenter > y2:
            closestY = y2
        else:
            closestY = yCenter

        return (closestX - xCenter)**2 + (closestY - yCenter)**2 <= radius**2