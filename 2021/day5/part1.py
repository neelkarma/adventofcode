from common import Line, Point, Board


if __name__ == "__main__":
    with open("./input.txt", "r") as inputFile:
        lines = filter(
            lambda line: line.start.x == line.end.x or line.start.y == line.end.y,
            [
                Line(
                    *[
                        Point(*[int(coord) for coord in coords.split(",")])
                        for coords in line.split(" -> ")
                    ]
                )
                for line in inputFile.readlines()
            ],
        )

        board = Board()

        for line in lines:
            board.process(line)

        print(board.countOverlaps())
