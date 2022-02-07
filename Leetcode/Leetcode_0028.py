#Implement strStr().

#Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

#Clarification:

#What should we return when needle is an empty string? This is a great question to ask during an interview.

#For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        
        if needle == "":
            return 0
        
        if needle in haystack:
            for i in range(len(haystack)):
                if haystack[i:i+len(needle)] == needle: #If the needle is found in the interval the range of the length of the needle, the index is returned.
                    return i
        else:
            return -1

        
        
        #Time complexity: O(n)
        #Space complexity: O(n)
