from statistics import median

if __name__ == "__main__":
    with open("./input.txt", "r") as inputFile:
        crabs = [int(crab) for crab in inputFile.readline().strip().split(",")]
        medianPosition = median(crabs)
        print(sum(abs(medianPosition - crab) for crab in crabs))
