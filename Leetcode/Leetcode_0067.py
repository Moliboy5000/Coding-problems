# Given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        #Turn the nums into ints in a list
        a = [int(nums) for nums in a]
        b = [int(nums) for nums in b]
        
        #If one list is longer, add leading zeroes
        if len(a) != len(b):
            for i in range((len(max(a,b,key=len))-len(min(a,b,key=len)))):
                min(a,b,key=len).insert(0,0)
        
        
        
        
        #Add lists
        res_array = []
        for i in range(len(a)):
            res_array.append(a[i] + b[i])

        for i in range(len(res_array)-1,-1,-1):
            if i != 0 and res_array[i] > 1: #If the sum in one index is more than one, one is added to the next position
                res_array[i] -= 2
                res_array[i-1] += 1
            
        
            elif res_array[i] > 1 and i == 0: #If index is first and sum is more than one, add additional 1 to list
                res_array[i] -= 2
                res_array.insert(0,1)
        
        res = ""
        
        for nums in res_array:
            res += str(nums)
            
        return res
        
        
        
        #Time complexity: O(n)
        #Space complexity: O(n)
        
                
            
            
            
        
        

            
        
            
            
            
            
            
        
