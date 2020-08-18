# creates board
def create_board(width, height):
    board = []
    for i in range(height):
        board.append([])
        for x in range(width):
            board[i].append(None)
    return board


# buries mines on the board
import random


def bury_mines(board, n):
    x = 0
    while x != n:
        random1 = random.randint(0, len(board) - 1)
        random2 = random.randint(0, len(board[0]) - 1)
        if board[random1][random2] == -1:
            continue
        else:
            x = x + 1
            board[random1][random2] = -1


# returns count of mines
def get_mine_count(board, x, y):
    z = 0
    for i in range(x - 1, x + 2, 1):
        if i == x:
            continue
        if i < 0 or i > len(board[0]) - 1:
            continue
        elif board[y][i] == -1:
            z = z + 1
    for j in range(x - 1, x + 2, 1):
        if j < 0 or j > len(board[0]) - 1 or y + 1 > len(board) - 1:
            continue
        elif board[y + 1][j] == -1:
            z = z + 1
    for k in range(x - 1, x + 2, 1):
        if k < 0 or k > len(board[0]) - 1 or y - 1 < 0:
            continue
        elif board[y - 1][k] == -1:
            z = z + 1
    return z


# prints board in row-column
def print_mines(board):
    for y in range(len(board)):
        element = ""
        for x in range(len(board[0])):
            if board[y][x] == None:
                element += "{:^5}\t".format('*')
            else:
                element += "{:^5}\t".format('.')
        print()
        print(element)

        # prints the board with mines and surrounding blocks with formatting
def print_board(board):
    for y in range(len(board)):
        element = ""
        for x in range(len(board[0])):
            if board[y][x] == None:
                element += "{:^5}\t".format(str(get_mine_count(board, x, y)))
            else:
                element += "{:^5}\t".format(str(board[y][x]))
        print(element)

        # changes the board based on user click
def uncover_board(board, x, y):
    if board[y][x] != None or board[y][x] == -1:
        return None
    elif board[y][x] != -1 and get_mine_count(board, x, y) >= 1:
        board[y][x] = get_mine_count(board, x, y)
    elif board[y][x] != -1 and get_mine_count(board, x, y) == 0:
        board[y][x] = 0
        for i in range(x - 1, x + 2, 1):
            if i == x:
                continue
            if i < 0 or i > len(board[0]) - 1:
                continue
            else:
                uncover_board(board, i, y)
        for j in range(x - 1, x + 2, 1):
            if j < 0 or j > len(board[0]) - 1 or y + 1 > len(board) - 1:
                continue
            else:
                uncover_board(board, j, y + 1)
        for k in range(x - 1, x + 2, 1):
            if k < 0 or k > len(board[0]) - 1 or y - 1 < 0:
                continue
            else:
                uncover_board(board, k, y - 1)

            # displays the board as the user sees it
def user_view(board):
    element = "{:^5}\t".format(" ")
    lines = "{:^5}\t".format(" ")
    for i in range(len(board[0])):
        element += "{:^5}\t".format(str(i))
        lines += "{:^5}\t".format('-')
    print(element)
    print(lines)

    for y in range(len(board)):
        element = "{:^5}\t".format(str(y) + '|')
        for x in range(len(board[0])):
            if board[y][x] == None or board[y][x] == -1:
                element += "{:^5}\t".format('?')
            elif board[y][x] >= 1:
                element += "{:^5}\t".format(str(board[y][x]))
            else:
                element += "{:^5}\t".format('.')
        print()
        print(element)

                # check if won
def check_won(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if y == len(board) - 1 and x == len(board[0]) - 1 and board[y][x] != None:
                return True
                break
            elif board[y][x] != None:
                continue
            else:
                return False
                break

                # getting close to the game
import time
def game(width, height, n):
    board = create_board(width, height)
    bury_mines(board, n)
    start_time = time.time()
    while not check_won(board):
        print("Time:", int(time.time() - start_time), "s")
        user_view(board)
        coor = str(input("Please enter coordinates"))
        x = int(coor[0])
        y = int(coor[2])
        if board[y][x] == -1:
            print("You hit a mine!")
            print_mines(board)
            break
        uncover_board(board, x, y)
    if check_won(board) is True:
        uncover_board(board, x, y)
        user_view(board)
        print("You Win!")



                        # Main Program
game(8, 8, 12)


