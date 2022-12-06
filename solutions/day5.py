import re


def create_stacks(stack_input):
    stacks = [[] for _ in range(len(stack_input[0][1::4])+1)]
    for s in stack_input:
        for k, v in enumerate(s[1::4], 1):
            if v.isalpha():
                stacks[k].append(v)

    return stacks


def part_1(instructions, stacks):
    for instruction in instructions:
        # pop item from the 'from' stack, append it to the 'to' stack
        for move in range(instruction[0]):
            stacks[instruction[2]].append(stacks[instruction[1]].pop(-1))

    return ''.join([stack[-1] for stack in stacks[1:]])


def part_2(instructions, stacks):
    for instruction in instructions:
        # pop item from the 'from' stack, append it to an intermediate stack
        intermediate_stack = []
        for move in range(instruction[0]):
            intermediate_stack.append(stacks[instruction[1]].pop(-1))
        stacks[instruction[2]].extend(reversed(intermediate_stack))

    return ''.join([stack[-1] for stack in stacks[1:]])


with open("../inputs/day5.txt") as file:
    input_data = file.read().splitlines()
    # separate initial stack data from instruction input
    stack_data = list(reversed(input_data[:input_data.index('')-1]))

    # return each instruction as a list of ints - follows the format [0=move, 1=from, 2=to]
    instruction_data = list(map(lambda i: list(map(int, filter(None, re.split(r'\D+', i)))),
                                input_data[input_data.index('')+1:]))

initial_stacks = create_stacks(stack_data)
print("Part 1 answer:", part_1(instruction_data, initial_stacks))
print("Part 2 answer:", part_2(instruction_data, initial_stacks))
