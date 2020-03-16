A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[7,4,1],[8,5,2],[9,6,3]]

def rotate_90(A):

    result = [[0,0,0],[0,0,0],[0,0,0]]

    for y in range(len(A)):

        for x in range(len(A[0])):

            result[y][x] = A[x][y]

    for t in range(len(result)):
        result[t] = result[t][::-1]

    print(result)
    return result

if rotate_90(A) == B:
    print("Pass!")
else:
    print("Fail.")

# An Inplace function to rotate
# N x N matrix by 90 degrees in
# anti-clockwise direction
def rotateMatrix(mat):
    # Consider all squares one by one
    N = len(mat[0])
    layers = N//2

    for x in range(0, layers):

        # Consider elements in group
        # of 4 in current square
        for y in range(x, N - x - 1):
            # store current cell in temp variable
            aux1 = mat[x][y]
            aux2 = mat[y][N-1-x]  # N-1 es el tamaño del array menos 1 que es el limite
            aux3 = mat[N-1-x][N-1-y]
            aux4 = mat[N-1-y][x]

            mat[x][y] = aux4
            mat[y][N-1-x] = aux1
            mat[N-1-x][N-1-y] = aux2
            mat[N-1-y][x] = aux3

def displayMatrix(mat):
    for i in range(0, len(mat)):
        for j in range(0, len(mat)):
            print(mat[i][j], end=' ')
        print("")


mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

rotateMatrix(mat)
displayMatrix(mat)