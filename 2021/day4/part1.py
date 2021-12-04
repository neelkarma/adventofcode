import itertools
from common import Board


if __name__ == "__main__":
    with open("./input.txt", "r") as inputFile:
        lines = [line.strip() for line in inputFile.readlines()]
        deck = [int(num) for num in lines.pop(0).split(",")]
        lines.pop(0)
        boards = {
            id: Board(list(board))
            for id, (isBlank, board) in enumerate(
                itertools.groupby(lines, lambda x: x == "")
            )
            if not isBlank
        }

        isWin = False
        lastNum = -1
        uncheckedSum = -1
        winBoard = None
        for num in deck:
            for id, board in list(boards.items()):
                board.checkDraw(num)
                if not board.checkWin():
                    continue
                winBoard = board
                lastNum = num
                isWin = True
                uncheckedSum = winBoard.sumUnchecked()
                break
            if isWin:
                break

        print(lastNum * uncheckedSum)
