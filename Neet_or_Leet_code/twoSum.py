# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution:
    def twoSum(self, nums, target):
        # for i in range(len(nums)):
        existed = {}
        for index, val in enumerate(nums):
            if target - val in existed:
                return [existed[target-val], index]
            existed[val] = index

s = Solution()
print(s.twoSum([2,7,11,15], 9))
value = True
res = value or "default"
print(res)
def checkmaxVal(a,b):
    return a if a > b else b
print(res == 1 and checkmaxVal(10, 20))

items = [ 0, -1, -23, 10]

# any method
found = any(item > 0 for item in items)
print(found)

# all method
found = all(item > 0 for item in items)
print(found)
