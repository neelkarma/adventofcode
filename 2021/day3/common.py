from typing import List


def bitCount(diagnostics: List[str], i: int):
    ones = 0
    zeroes = 0
    for line in diagnostics:
        if line[i] == "1":
            ones += 1
        else:
            zeroes += 1
    return ones, zeroes
