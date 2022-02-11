#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
#The digits are ordered from most significant to least significant in left-to-right order.
#The large integer does not contain any leading 0's.

#Increment the large integer by one and return the resulting array of digits.



class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        
        
        
        for i in range(1,len(digits)+1):
            digits[len(digits)-i] += 1
            if digits[len(digits)-i] == 10: # If adding one makes the number equal to ten, then the digit is set to zero and the loop continues.
                digits[len(digits)-i] = 0
            else:
                return digits
        
        #For when all digits are nines.
        digits[0] = 0
        digits.insert(0,1)
        return digits
                
            
            
        #Time complexity: O(n)
        #Space complexity: O(n)
      
            
        
            
        
