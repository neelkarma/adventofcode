from typing import Dict


def simulateFish(fishCounter: Dict[int, int], days: int):
    for _ in range(days):
        newFishCounter = {i: 0 for i in range(9)}
        for timer, count in fishCounter.items():
            if timer == 0:
                newFishCounter[6] += count
                newFishCounter[8] += count
                continue
            newFishCounter[timer - 1] += count
        fishCounter = newFishCounter
    return sum(fishCounter.values())
