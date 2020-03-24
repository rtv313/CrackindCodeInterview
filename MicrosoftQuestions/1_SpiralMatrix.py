

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]


def travers_matrix_spiral(matrix):

    length = len(matrix)
    layers = length // 2
    top_limit = 0
    bottom_limit = length - 1
    left_limit = 0
    right_limit = length

    while left_limit < length and top_limit < length:

        for x in range(left_limit,right_limit):
            print(matrix[left_limit][x])

        top_limit += 1

        for x in range(top_limit,bottom_limit + 1):
            print(matrix[x][right_limit - 1])

        right_limit -= 1


        for x in range(right_limit - 1,left_limit - 1,-1):
            print(matrix[bottom_limit][x])

        bottom_limit -= 1

        for x in range(bottom_limit,top_limit - 1,-1):
            print(matrix[x][left_limit])

        left_limit += 1

travers_matrix_spiral(matrix)