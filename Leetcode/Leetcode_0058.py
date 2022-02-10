#Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

#A word is a maximal substring consisting of non-space characters only.

 


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s_arr = []
        
        for chars in s:
            s_arr.append(chars) #Add every character to list
            
        
        while s_arr[len(s_arr)-1] == " ": #Delete all spaces at the end
            s_arr.pop(len(s_arr)-1)
        
        if " " not in s_arr: #If there is only one word in the list, return the length of the single word.
            return len(s_arr)
        
        for i in range(len(s_arr)):
            if s_arr[i-1] == " " and " " not in s_arr[i:len(s_arr)]: #If there is no space at the rest of the interval, then the word is the last word.
                return len(s_arr[i:len(s_arr)])
              
        
        #Time complexity: O(n)
        #Space complexity: O(n)
        
        
        
