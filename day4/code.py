def readInput():
    file = open("input.txt", "r")
    boards = []
    for i, line in enumerate(file):
        line = line.strip()
        if i == 0:
            numbers = [int(a) for a in line.split(",")]
            continue
        if line == "":
            if i != 1:
                boards.append(board)
            board = []
            continue
        else:
            board.append([int(a) for a in line.split()])
    boards.append(board)
    file.close()
    return numbers, boards

def markBoard(board, n):
    newBoard = []
    for row in board:
        newRow = []
        for num in row:
            if num == n:
                newRow.append(-1)
            else:
                newRow.append(num)
        newBoard.append(newRow)
    return newBoard

def checkWin(board):
    # check rows
    for row in board:
        for num in row:
            if num >= 0:
                break
        else:
            return True
    # check colums
    for x in range(5):
        for y in range(5):
            if board[y][x] >= 0:
                break
        else:
            return True
    return False

def sumBoard(board):
    out = 0
    for row in board:
        for num in row:
            out += num if num >= 0 else 0
    return out

def printBoard(board):
    print("[", end="")
    for row in board:
        print(row)

def main():
    numbers, boards = readInput()
    for num in numbers:
        winner = []
        for i in range(len(boards)):
            boards[i] = markBoard(boards[i], num)
            printBoard(boards[i])
            if checkWin(boards[i]):
                winner.append(i)
        deleted = []
        for i in winner:
            if len(boards) == 1:
                print(sumBoard(boards[i]) * num)
                print(num)
                print(sumBoard(boards[i]))
                return
            offset = [1 for a in deleted if a < i]
            boards.pop(i-sum(offset))
            deleted.append(i)
main()
