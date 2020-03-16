# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0,

def display_matrix(matrix):
    for i in range(0,len(matrix)):

        for j in range(0,len(matrix)):
            print(matrix[i][j], end=' ')

        print("")



def convert_row_and_column(row,column,matrix):

    for x_column  in range(0,len(matrix)):
        matrix[row][x_column] = 0

    for x_row in range(0,len(matrix)):
        matrix[x_row][column] = 0


def zero_matrix(matrix):
    matrix_clone  = matrix.copy()

    for row in range(0,len(matrix_clone)):
        for column in range(0,len(matrix_clone)):
            if matrix_clone[row][column] == 0:
                convert_row_and_column(row,column,matrix)
    return matrix

matrix = [[1,1,1,1],
          [0,1,1,1],
          [1,1,0,1],
          [0,1,1,1]]

display_matrix(matrix)
zero_matrix(matrix)
print("#########################")
display_matrix(matrix)