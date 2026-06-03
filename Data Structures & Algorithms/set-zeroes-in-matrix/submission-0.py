class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        zeros = []

        # First pass: find all original zeros
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros.append((i, j))

        # Second pass: zero rows and columns
        for i, j in zeros:

            # Zero the row
            matrix[i] = [0] * len(matrix[0])

            # Zero the column
            for k in range(len(matrix)):
                matrix[k][j] = 0