class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            row = [x for x in board[i] if x != '.']

            if len(row) != len(set(row)):
                return False


        for i in range(9):
            column = []

            for j in range(9):
                if board[j][i] != '.':
                    column.append(board[j][i])

            if len(column) != len(set(column)):
                return False


        for r in range(0, 9, 3):
            for c in range(0, 9, 3):

                square = []

                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        square.append(board[i][j])

                square = [x for x in square if x != '.']

                if len(square) != len(set(square)):
                    return False

        return True