# CW: Brute Forcing. Feel free to leave if you feel uncomfortable at any point.
from itertools import permutations


def allCombinations(*chars: str):
    return ["".join(comb) for comb in permutations(chars)]


if __name__ == "__main__":
    with open("./input.txt", "r") as inputFile:
        data = [
            [side.split() for side in line.strip().split(" | ")]
            for line in inputFile.readlines()
        ]
        outputSum = 0
        mapping = {
            "ab": 1,
            "abcdef": 9,
            "abcdefg": 8,
            "abcdeg": 0,
            "abcdf": 3,
            "abd": 7,
            "abef": 4,
            "acdfg": 2,
            "bcdef": 5,
            "bcdefg": 6,
        }
        for g1, g2 in data:
            for perm in permutations("abcdefg"):
                permMapping = {k: v for k, v in zip(perm, "abcdefg")}

                g1List = ["".join(permMapping[c] for c in x) for x in g1]
                g2List = ["".join(permMapping[c] for c in x) for x in g2]

                if all("".join(sorted(ans)) in mapping for ans in g1List):
                    g2List = ["".join(sorted(x)) for x in g2List]
                    outputSum += int("".join(str(mapping[x]) for x in g2List))
                    break

        print(outputSum)
