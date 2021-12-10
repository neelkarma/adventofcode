if __name__ == "__main__":
    with open("./input.txt", "r") as inputFile:
        lines = [line.strip() for line in inputFile.readlines()]
        chunkOpen = ["(", "[", "{", "<"]
        chunkClose = [")", "]", "}", ">"]
        chunkMap = {k: v for k, v in zip(chunkOpen, chunkClose)}
        invalidCharPoints = {k: v for k, v in zip(chunkClose, [3, 57, 1197, 25137])}
        points = 0
        for line in lines:
            stack = []
            for char in line:
                if char in chunkOpen:
                    stack.append(char)
                if char in chunkClose:
                    if chunkMap[stack[-1]] == char:
                        stack.pop()
                    else:
                        points += invalidCharPoints[char]
                        break
        print(points)
