def main():
    with open("../inputs/02.txt") as f:
        commands = [*map(str.split, f)]

    horizontal, depth = 0, 0

    for direction, amount in commands:
        amount = int(amount)
        match direction:
            case "up":
                depth -= amount
            case "down":
                depth += amount
            case "forward":
                horizontal += amount

    part1 = horizontal * depth
    assert part1 == 2102357

    horizontal, depth, aim = 0, 0, 0

    for direction, amount in commands:
        amount = int(amount)
        match direction:
            case "up":
                aim -= amount
            case "down":
                aim += amount
            case "forward":
                horizontal += amount
                depth += aim * amount

    part2 = horizontal * depth
    assert part2 == 2101031224


if __name__ == "__main__":
    main()
