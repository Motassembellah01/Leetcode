from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximWater = 0
        l = 0
        r = len(height) - 1
        while l < r:
            leftBar = height[l]
            rightBar = height[r]
            minHeight = min(leftBar, rightBar)
            width = r - l
            area = width * minHeight
            maximWater = max(maximWater, area)
            if leftBar < rightBar:
                l += 1
            else:
                r -= 1
        return maximWater