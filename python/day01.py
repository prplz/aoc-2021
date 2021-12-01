def main():
    with open("../inputs/01.txt") as f:
        values = [*map(int, f)]

    part1 = sum(b > a for a, b in zip(values, values[1:]))
    assert part1 == 1557

    part2 = sum(b > a for a, b in zip(values, values[3:]))
    assert part2 == 1608


if __name__ == "__main__":
    main()
