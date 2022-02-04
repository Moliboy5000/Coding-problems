#Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

#Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.



class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        
        nums_pos = { #Dictionary with strings corresponding to integers (not direct conversion)
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }
        
        
        def extendString(num): #Each number is multiplied individually in relation with its position in reverse so that the exponent is correct.
            mult = 0
            num_extended = 0
            for chars in num[::-1]:
                num_extended += (nums_pos[chars])*(10**mult)
                mult += 1
            return num_extended
        
        return str(extendString(num1) * extendString(num2))
            
            
        
