"""
 Two Sum II - Input Array Is Sorted (LeetCode 167) 
 Problem: Find two numbers in a sorted array that add up to a target value. Return 1-indexed positions.
 
 Use two pointers from both ends, adjust based on sum comparison with target.

"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:

            current = numbers[left] + numbers[right]
            if current == target:
                return [left + 1, right + 1] #1 based index
            if current < target:
                left += 1
            else:
                right -= 1
        return []

s = Solution()
print(s.twoSum([1,2,3,4,5,9], 7))
