#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

#Symbol       Value
#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000
#For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II.
#The number 27 is written as XXVII, which is XX + V + II.

#Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV.
#Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. 
#There are six instances where subtraction is used:

#I can be placed before V (5) and X (10) to make 4 and 9. 
#X can be placed before L (50) and C (100) to make 40 and 90. 
#C can be placed before D (500) and M (1000) to make 400 and 900.
#Given an integer, convert it to a roman numeral.
#Given a roman numeral, convert it to an integer.








class Solution:
    def romanToInt(self, s: str) -> int:
        
        
        combs = {  #Dicct with roman numerals corresponding to their numerical value
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }
        
        res = 0
        i = 0
        while i < len(s):
            if i != len(s)-1:
                if s[i] == "I" and s[i+1] == "V":   #In the exception cases mentioned above
                    i += 1
                    res += 4
                elif s[i] == "I" and s[i+1] == "X":
                    i += 1
                    res += 9
                elif s[i] == "X" and s[i+1] == "L":
                    i += 1
                    res += 40
                elif s[i] == "X" and s[i+1] == "C":
                    i += 1
                    res += 90
                elif s[i] == "C" and s[i+1] == "D":
                    i += 1
                    res += 400
                elif s[i] == "C" and s[i+1] == "M":
                    i += 1
                    res += 900
                else:
                    res += combs[s[i]]
            
            else:
                res += combs[s[i]]
            i += 1
        return res
            
        #Time complexity: O(n)
        #Space complexity: O(n)
        
