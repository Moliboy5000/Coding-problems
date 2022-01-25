








class Solution:
    def romanToInt(self, s: str) -> int:
        
        
        combs = {
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
                if s[i] == "I" and s[i+1] == "V":
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
            
            
        
