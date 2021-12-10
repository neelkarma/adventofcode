from statistics import median

if __name__ == "__main__":
    with open("./input.txt", "r") as inputFile:
        lines = [line.strip() for line in inputFile.readlines()]
        chunkOpen = ["(", "[", "{", "<"]
        chunkClose = [")", "]", "}", ">"]
        chunkMap = {k: v for k, v in zip(chunkOpen, chunkClose)}
        incompleteLines = []
        for line in lines:
            stack = []
            isCorrupted = False
            for char in line:
                if char in chunkOpen:
                    stack.append(char)
                if char in chunkClose:
                    if chunkMap[stack[-1]] == char:
                        stack.pop()
                    else:
                        isCorrupted = True
                        break
            if not isCorrupted:
                incompleteLines.append(line)

        pointMap = {k: v for k, v in zip(chunkClose, [1, 2, 3, 4])}
        scores = []
        for line in incompleteLines:
            stack = []
            for char in line:
                if char in chunkOpen:
                    stack.append(char)
                if char in chunkClose:
                    if chunkMap[stack[-1]] == char:
                        stack.pop()
            charPoints = [pointMap[chunkMap[char]] for char in reversed(stack)]
            score = 0
            for point in charPoints:
                score *= 5
                score += point
            scores.append(score)
        print(median(scores))
