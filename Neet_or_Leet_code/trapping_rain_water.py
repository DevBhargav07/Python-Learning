"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array 
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.


"""
class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        total_water = 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                total_water += left_max - height[left]
                print("left max",left_max, height[left], total_water)
                left += 1
            else:
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]
                print("right max",right_max, height[right], total_water)
                right -= 1
        return total_water


if __name__ == "__main__":
    s = Solution()
    print(s.trap( [0,2,0,3,1,0,1,3,2,1]))
