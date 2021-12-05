from math import log2, ceil
from functools import reduce


def main():
    with open("../inputs/03_test.txt") as f:
        test_values = [int(line, 2) for line in f]

    assert part1(test_values) == 198
    assert part2(test_values) == 230

    with open("../inputs/03.txt") as f:
        values = [int(line, 2) for line in f]

    assert part1(values) == 4001724
    assert part2(values) == 587895


def part1(values):
    bits = ceil(log2(max(values)))
    epsilon = sum(
        (sum((x >> bit) & 1 for x in values) >= len(values) / 2) << bit
        for bit in range(bits)
    )
    gamma = ~epsilon & ((1 << bits) - 1)
    return epsilon * gamma


def part2(values):
    bits = ceil(log2(max(values)))
    result = 1
    for polarity in 0, 1:
        candidates = values
        for bit in reversed(range(bits)):
            commonest = sum(x & (1 << bit) != 0 for x in candidates) >= len(candidates) / 2
            candidates = [x for x in candidates if (x >> bit) & 1 == commonest ^ polarity]
            if len(candidates) == 1:
                break
        (winning_ticket,) = candidates
        result *= winning_ticket
    return result


if __name__ == "__main__":
    main()
