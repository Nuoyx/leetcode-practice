class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_valid_set_array = [set() for _ in range(9)]
        col_valid_set_array = [set() for _ in range(9)]
        grid_valid_set_array = [set() for _ in range(9)]

        for row in range(len(board)):
            for col in range(len(board[0])):
                value = board[row][col]
                if(value != "."):
                    if(value in row_valid_set_array[row]):
                        return False
                    else:
                        row_valid_set_array[row].add(value)

                    if(value in col_valid_set_array[col]):
                        return False
                    else:
                        col_valid_set_array[col].add(value)
                    
                    grid_row = row // 3
                    grid_col = col // 3
                    grid_index = grid_row * 3 + grid_col
                    if(value in grid_valid_set_array[grid_index]):
                        return False
                    else:
                        grid_valid_set_array[grid_index].add(value)
        return True