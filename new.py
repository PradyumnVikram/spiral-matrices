__author__ = 'Pradyumn Vikram'

board = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]


def removeBoundary(matrix, m, n):
    array = []
    total = 4 * (n - 1)
    last_done = False
    for row_ind, row in enumerate(matrix):
        if row_ind == 0:
            for val in row:
                array.append(val)
        elif row_ind == n-1:
            for val in row[::-1]:

                last_done = True
                array.append(val)
        elif row_ind < total//2:
            array.append(row[n - 1])

        if last_done:
            j = n - 2
            while j > 0 and j < n - 1:
                array.append(matrix[j][0])

                j -= 1
    new_board = []
    for row in board[1:n-1]:
        new_board.append(row[1:n-1])

    return array, new_board


def print_board(board, n, a):
    if n % 2 != 0:
        val = (board[((n+1)//2) - 1][((n+1)//2) - 1])
    while n >= 0:
        array, board = removeBoundary(board, n, n)
        a += array
        n -= 2
    if n % 2 != 0:
        a[-1] = val
    return a


def main(board, n):
    ans = print_board(board, n, [])
    for i in ans:
        print(i, end=' ')


main(board, len(board))
