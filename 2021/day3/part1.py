# There is probably a better way to do this, but I'm not bothered to find it

if __name__ == "__main__":
    with open("./input.txt", "r") as inputFile:
        diagnostics = [line.strip() for line in inputFile.readlines()]
        gammaBin = ""

        for i, _ in enumerate(diagnostics[0]):
            ones = 0
            zeroes = 0
            for line in diagnostics:
                if line[i] == "1":
                    ones += 1
                else:
                    zeroes += 1
            gammaBin += "1" if ones > zeroes else "0"

        epsilonBin = "".join(["0" if bit == "1" else "1" for bit in gammaBin])

        gamma = int(gammaBin, 2)
        epsilon = int(epsilonBin, 2)
        print(gamma * epsilon)
