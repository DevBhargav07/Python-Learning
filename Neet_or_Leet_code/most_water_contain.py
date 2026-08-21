"""

Container With Most Water (LeetCode 11)

Problem: Given array of heights, find two lines that form container holding the most water.

Approach: Two pointers from both ends, move pointer with shorter height inward to potentially find larger area.

"""
class Solution:
    def maxWater(self, height: list[int]) -> int:
        left = 0
        right = len(height) -1
        maxArea = 0
        while left < right:
            minHeight = min(height[left], height[right])
            width = right - left
            product = minHeight * width

            maxArea = max(maxArea, product)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea

s = Solution()
print(s.maxWater([1, 8, 6,2,5,4,8,3,7]))
