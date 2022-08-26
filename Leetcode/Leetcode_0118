#Given an integer numRows, return the first numRows of Pascal's triangle.
#In Pascal's triangle, each number is the sum of the two numbers directly above.


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]] 
        triangle = [[1],[1,1]] #Create first rows manually to work with algorithm
        
        for i in range(numRows-2): #Since first two rows were created manually, subtract 2 from rows to generate
            newRow = [1] #Every row starts with 1
            for j in range(len(triangle[len(triangle)-1])): #Creates new row from numbers in previous row
                
                if j+1 == len(triangle[len(triangle)-1]):
                    break #To avoid list index out of range
                newRow.append(triangle[len(triangle)-1][j] + triangle[len(triangle)-1][j+1]) #Appends the sum of number at index j and the number to the right
            
            newRow.append(1) #Every row ends with 1
            triangle.append(newRow)
        
        return triangle
        
        #Time complexity: O(n^2)
        #Space complexity: O(n)
