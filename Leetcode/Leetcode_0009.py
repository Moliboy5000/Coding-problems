#Given an integer x, return true if x is palindrome integer.

#An integer is a palindrome when it reads the same backward as forward.

#For example, 121 is a palindrome while 123 is not.
 






class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x) #Convert to string to allow reversing
        if num[::-1] == num: #Chekcs if the reversed string is equal to the normal string, making it a palindrome.
            return True
        else:
            return False
        
#Time complexity: O(n)
#Space complexity: O(n)
