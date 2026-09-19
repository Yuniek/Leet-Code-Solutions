"1401. Circle and Rectangle Overlapping"
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        return (xCenter-min(max(x1, xCenter), x2))**2+(yCenter-min(max(y1, yCenter), y2))**2 <= radius**2

print(Solution().checkOverlap(1,0,0,1,-1,3,1))