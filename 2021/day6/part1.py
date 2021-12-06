from collections import Counter
from common import simulateFish

if __name__ == "__main__":
    with open("./input.txt", "r") as inputFile:
        fishes = [int(timer) for timer in inputFile.readline().strip().split(",")]
        fishCounter = dict(Counter(fishes))
        print(simulateFish(fishCounter, 80))
