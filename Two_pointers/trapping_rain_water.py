from typing import List


# Optimal solution submitted
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        l = 0
        r = n - 1
        leftMax = height[l]
        rightMax = height[r]
        traps = 0

        while l < r:
            if leftMax <= rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                traps += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                traps += rightMax - height[r]
        
        return traps


# First working solution
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        counter = 0
        leftMax = [0] * n
        rightMax = [0] * n

        for i in range(1, n):
            leftMax[i] = max(height[i - 1], leftMax[i - 1])

        for i in range(n - 2, -1, -1):
            rightMax[i] = max(height[i + 1], rightMax[i + 1])
        
        for i in range(n):
            maxHeightWater = min(leftMax[i], rightMax[i])
            realHeightWater = maxHeightWater - height[i]
            if realHeightWater > 0:
                counter += realHeightWater
        
        return counter