# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above.






class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        #First rows expressed manually to work with algorithm
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        #First two rows
        triangle = [[1],[1,1]]
        
        #Generates triangle, see previous problem for details
        for i in range(rowIndex-1):
            newRow = [1]
            for j in range(len(triangle[len(triangle)-1])):
                if j+1 == len(triangle[len(triangle)-1]):
                    break
                newRow.append(triangle[len(triangle)-1][j] +triangle[len(triangle)-1][j+1])
            newRow.append(1)
            triangle.append(newRow)
        
        return triangle[rowIndex]
      
      # Time complexity: O(n^2)
      # Space complexity: O(n)
        
        
