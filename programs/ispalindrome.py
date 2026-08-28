"""
Valid Palindrome (LeetCode 125)

Problem: Check if a string is a palindrome, considering only alphanumeric characters and ignoring case.


Use two pointers from both ends, skip non-alphanumeric characters, compare values.

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0 # left index
        j = len(s) - 1 # right index
        while i < j:

            while i < j and not s[i].isalnum():
                i += 1
            
            while i < j and not s[j].isalnum():
                j -= 1
            
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

s = Solution()
print(s.isPalindrome("Madam"))
