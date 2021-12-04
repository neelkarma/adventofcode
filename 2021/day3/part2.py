from typing import List
from common import bitCount


def calculateOxygen(diagnostics: List[str]):
    for i, _ in enumerate(diagnostics[0]):
        if len(diagnostics) == 1:
            break
        ones, zeroes = bitCount(diagnostics, i)
        filterValue = "1" if ones >= zeroes else "0"
        diagnostics = [line for line in diagnostics if line[i] == filterValue]
    return diagnostics[0]


def calculateCarbon(diagnostics: List[str]):
    for i, _ in enumerate(diagnostics[0]):
        if len(diagnostics) == 1:
            break
        ones, zeroes = bitCount(diagnostics, i)
        filterValue = "0" if zeroes <= ones else "1"
        diagnostics = [line for line in diagnostics if line[i] == filterValue]
    return diagnostics[0]


if __name__ == "__main__":
    with open("./input.txt", "r") as inputFile:
        diagnostics = [line.strip() for line in inputFile.readlines()]
        oxygen = int(calculateOxygen(diagnostics), 2)
        carbon = int(calculateCarbon(diagnostics), 2)
        print(oxygen * carbon)
