from common import simulateFish

if __name__ == "__main__":
    with open("./input.txt", "r") as inputFile:
        fishes = [int(timer) for timer in inputFile.readline().strip().split(",")]
        fishCounter = {i: fishes.count(i) for i in range(9)}
        print(simulateFish(fishCounter, 256))
