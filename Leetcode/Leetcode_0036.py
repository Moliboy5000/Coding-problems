#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#Note:

#A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#Only the filled cells need to be validated according to the mentioned rules.


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #A Sudoku board is valid if there is no same number horizontally, vertically and in the same 3x3 box.
        
        
        for i in range(9): #Iterate horizontally
            nums = [] #Each new number is added to the array, if the same number is found again, then the board is not valid.
            for j in range(9):
                if board[i][j] in nums:
                    return False
                elif board[i][j] != ".":
                    nums.append(board[i][j])
                    
                    
        for i in range(9): #Iterate vertically
            nums = []
            for j in range(9):
                if board[j][i] in nums:
                    return False
                elif board[j][i] != ".":
                    nums.append(board[j][i])
                    
                    
                    
        
        lower = 0
        upper = 3
        for k in range(3):
        
            for m in range(2,9,3):
                nums = []
                box = board[m-2][lower:upper] + board[m-1][lower:upper] + board[m][lower:upper] #Checks each 3x3 box by adding the 3 rows to an array and iterating through it.
                for j in box:
                    if j in nums:
                        return False
                    elif j != ".":
                        nums.append(j)
            lower += 3
            upper += 3
            
        return True
            
            
        
        
         #Time complexity: O(n^2)
         #Space complexity: O(n)
            
            
                
            
            
            
            
            
        
