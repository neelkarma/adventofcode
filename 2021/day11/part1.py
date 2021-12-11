if __name__ == "__main__":
    with open("./input.txt", "r") as input_file:
        grid = [[int(char) for char in line.strip()] for line in input_file.readlines()]
        total_flashes = 0
        for _ in range(100):
            for y, row in enumerate(grid):
                for x, _ in enumerate(row):
                    grid[y][x] += 1

            curr_step_flashes = []
            queue = []
            for y, row in enumerate(grid):
                for x, energy in enumerate(row):
                    if energy > 9:
                        queue.append((x, y))

            while queue:
                x, y = queue.pop(0)
                if (x, y) in curr_step_flashes:
                    continue
                curr_step_flashes.append((x, y))
                if x + 1 < len(grid[0]):
                    if not (x + 1, y) in curr_step_flashes:
                        grid[y][x + 1] += 1
                        if grid[y][x + 1] > 9:
                            queue.append((x + 1, y))
                if x - 1 >= 0:
                    if not (x - 1, y) in curr_step_flashes:
                        grid[y][x - 1] += 1
                        if grid[y][x - 1] > 9:
                            queue.append((x - 1, y))
                if y + 1 < len(grid):
                    if not (x, y + 1) in curr_step_flashes:
                        grid[y + 1][x] += 1
                        if grid[y + 1][x] > 9:
                            queue.append((x, y + 1))
                if y - 1 >= 0:
                    if not (x, y - 1) in curr_step_flashes:
                        grid[y - 1][x] += 1
                        if grid[y - 1][x] > 9:
                            queue.append((x, y - 1))
                if x + 1 < len(grid[0]) and y - 1 >= 0:
                    if not (x + 1, y - 1) in curr_step_flashes:
                        grid[y - 1][x + 1] += 1
                        if grid[y - 1][x + 1] > 9:
                            queue.append((x + 1, y - 1))
                if x + 1 < len(grid[0]) and y + 1 < len(grid):
                    if not (x + 1, y + 1) in curr_step_flashes:
                        grid[y + 1][x + 1] += 1
                        if grid[y + 1][x + 1] > 9:
                            queue.append((x + 1, y + 1))
                if x - 1 >= 0 and y + 1 < len(grid):
                    if not (x - 1, y + 1) in curr_step_flashes:
                        grid[y + 1][x - 1] += 1
                        if grid[y + 1][x - 1] > 9:
                            queue.append((x - 1, y + 1))
                if x - 1 >= 0 and y - 1 >= 0:
                    if not (x - 1, y - 1) in curr_step_flashes:
                        grid[y - 1][x - 1] += 1
                        if grid[y - 1][x - 1] > 9:
                            queue.append((x - 1, y - 1))
            for x, y in curr_step_flashes:
                grid[y][x] = 0

            total_flashes += len(curr_step_flashes)
        print(total_flashes)
