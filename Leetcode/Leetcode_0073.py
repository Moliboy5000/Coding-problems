# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

#You must do it in place.




class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        originals = []
        
        for i in range(len(matrix)): #First loop stores index of original zeroes, so that the program only checks for original zeroes
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    originals.append([i,j])
                    
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0 and [i,j] in originals: #If index belongs to original zeroes
                    for k in range(len(matrix[i])): #Change entire row to zeroes
                        if matrix[i][k] != 0:
                            matrix[i][k] = 0
                            
                    if i != 0: #Change colums above to zero
                        for k in range(0,i):
                            matrix[k][j] = 0
                    if i != len(matrix)-1: #Change columns below to zero
                        for k in range(i+1,len(matrix)):
                            matrix[k][j] = 0
                            

 #Time complexity: O(n^2)
 #Space complexity: O(n)
                
