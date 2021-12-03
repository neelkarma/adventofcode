if __name__ == "__main__":
    with open("./input.txt", "r") as inputFile:
        data = [int(line) for line in inputFile.readlines()]
        increments = 0
        for i, _ in enumerate(data[1:]):
            if data[i] > data[i - 1]:
                increments += 1
        print(increments)
