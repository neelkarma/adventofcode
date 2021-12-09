if __name__ == "__main__":
    with open("./input.txt", "r") as inputFile:
        data = [
            [side.split() for side in line.strip().split(" | ")]
            for line in inputFile.readlines()
        ]
        uniqueCount = 0
        for line in data:
            for display in line[1]:
                if len(display) in [2, 4, 3, 7]:
                    uniqueCount += 1
        print(uniqueCount)
