if __name__ == "__main__":
    with open("./input.txt", "r") as inputFile:
        grid = [
            [int(point) for point in line]
            for line in [line.strip() for line in inputFile.readlines()]
        ]
        totalRisk = 0
        for y, rows in enumerate(grid):
            for x, point in enumerate(rows):
                if (
                    (point < grid[y + 1][x] if y + 1 < len(grid) else True)
                    and (point < grid[y - 1][x] if y - 1 >= 0 else True)
                    and (point < grid[y][x + 1] if x + 1 < len(rows) else True)
                    and (point < grid[y][x - 1] if x - 1 >= 0 else True)
                ):
                    totalRisk += point + 1
        print(totalRisk)
