class Solution(object):
    def rotate(self, matrix):
        empty = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row != col and [row, col] not in empty:
                    matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
                    empty.extend([[col, row]])
        for element in matrix:
            element.reverse()

        return matrix