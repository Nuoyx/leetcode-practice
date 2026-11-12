class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        target_col = set()
        target_row = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    target_col.add(col)
                    target_row.add(row)

        
        for row in target_row:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0
        
        for col in target_col:
            for row in range(len(matrix)):
                matrix[row][col] = 0

                
                
                