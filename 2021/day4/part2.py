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

        isLose = False
        lastNum = -1
        uncheckedSum = -1
        loseBoard = None

        for num in deck:
            for id, board in list(boards.items()):
                board.checkDraw(num)
                if not board.checkWin():
                    continue
                if not len(boards) == 1:
                    boards.pop(id)
                    continue
                loseBoard = board
                isLose = True
                lastNum = num
                uncheckedSum = loseBoard.sumUnchecked()
                break
            if isLose:
                break

        print(lastNum * uncheckedSum)
