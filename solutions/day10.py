def part_1(instructions):
    clock = 1
    register_value = 1
    next_signal = 20
    signal_strengths = []

    for ins in instructions:
        if clock == next_signal:
            signal_strengths.append(register_value * clock)
            next_signal += 40

        clock += 1
        if ins[0] == "addx":
            if clock == next_signal:
                signal_strengths.append(register_value * clock)
                next_signal += 40
            clock += 1
            register_value += int(ins[1])

    return sum(signal_strengths)


if __name__ in "__main__":
    with open('../inputs/day10.txt') as file:
        puzzle_input = [f.split() for f in file]

    print("part 1:", part_1(puzzle_input))
