# CW: Brute Forcing. Feel free to leave if you feel uncomfortable at any point.


def triangleSum(num: int):
    return sum([i for i in range(1, num + 1)])


if __name__ == "__main__":
    with open("./input.txt", "r") as inputFile:
        crabs = [int(crab) for crab in inputFile.readline().strip().split(",")]
        lowestFuelCost = float("inf")
        maxDistance = max(crabs)
        for i in range(0, maxDistance):
            print(f"Progress: {i}/{maxDistance}")
            fuelCost = sum(triangleSum(int(abs(i - crab))) for crab in crabs)
            if fuelCost < lowestFuelCost:
                lowestFuelCost = fuelCost
        print(lowestFuelCost)
