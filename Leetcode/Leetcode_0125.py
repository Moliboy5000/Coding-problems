# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #uses regex to filter out non-alphanumeric characters, also makes all characters lowercase
        s = re.sub(r'[\W_]+', '', s.lower())
        
        #If string is same backwards return true
        if s == s[::-1]:
            return True
        else:
            return False
          
          
          
          
          # Time complexity: O(n)
          # Space complexity: O(n)
          
          
          
          
        
