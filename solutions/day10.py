with open('../inputs/day10_test.txt') as file:
    instructions = [f.split() for f in file]

clock = 0
register_value = 1
next_signal = 20
signal_strengths = []
current_instruction = []
log_addx = []

while len(instructions) > 0:
    # fetch next instruction
    if len(current_instruction) == 0:
        current_instruction = instructions.pop(0)  # load next instruction

    # store addx value in register
    elif current_instruction[0] == "addx" and len(current_instruction) == 2:
        register_value += int(current_instruction.pop(1))
        current_instruction = []

    else:
        current_instruction = []  # clear instruction from cache

    if clock == next_signal:
        # signal_strengths.append(register_value * clock)
        signal_strengths.append((register_value, clock, register_value * clock))
        next_signal += 40

    clock += 1


print(signal_strengths)

