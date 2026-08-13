"""
Minimal jumps by frog to reach the end point
The Frog Jumping Staircase Problem is a classic algorithmic challenge where a frog must 
climb a staircase with n steps, each having a specific height.  
The goal is to find the minimum energy required to reach the top, where the energy cost to 
jump from step i to step j is the absolute difference in their heights,
"""

def minimumJump(ind, height):
    if ind == 0:
        return 0
    left = minimumJump(ind-1, height) + abs(height[ind] - height[ind -1])
    right = float("inf")
    if ind > 1: 
        right = minimumJump(ind-2, height)  + abs(height[ind] - height[ind -2])
    return min(left, right)

def minimumJumpMemo(ind, height, dp):
    """
        finding the jumps using recursion + memorization
    """
    if ind == 0:
        return 0
    if dp[ind] != -1:
        return dp[ind]
    left = minimumJumpMemo(ind-1, height, dp) + abs(height[ind] - height[ind - 1])
    right = float("inf")
    if ind > 1:
        right = minimumJumpMemo(ind - 2, height, dp) + abs(height[ind] - height[ind - 2])
    dp[ind] = min(left, right)
    return dp[ind]
    

if __name__ == "__main__":
    heights = [10, 20, 30, 10]
    lastindex = len(heights) - 1
    dp = [-1] * (lastindex + 1)
    print("Using recursion",minimumJump(lastindex, heights))
    print("Using recursion with memorization",minimumJumpMemo(lastindex, heights, dp))
    # using tabulation method to not use recursion
    dp2 = [0] * (lastindex + 1)
    for i in range(1, lastindex):
        left = dp2[i-1] + abs(heights[i] - heights[i-1])
        right = float("inf")
        if i > 1:
            right = dp2[i-2] + abs(heights[i] - heights[i-2])
        dp2[i] = min(left, right)
    print("Using tabulation method",dp2[lastindex-1])
    # using tabulation wwithout dp
    prev2i, previ = 0, 0
    for i in range(1, lastindex):
        left = previ + abs(heights[i] - heights[i-1])
        right = float("inf")
        if i > 1:
            right = prev2i + abs(heights[i] - heights[i-2])
        curi = min(left, right)
        prev2i = previ
        previ = curi
    print("Using tabulation with space complexity: ", previ)

