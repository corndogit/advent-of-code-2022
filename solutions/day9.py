with open('../inputs/day9_test.txt') as file:
    instructions = [f.split() for f in file.read().splitlines()]


def parse_move(direction: str, is_horizontal: bool) -> int:
    if is_horizontal:
        if direction == 'R':
            return 1
        elif direction == 'L':
            return -1
        else:
            return 0
    else:
        if direction == 'U':
            return 1
        elif direction == 'D':
            return -1
        else:
            return 0


# end_coord = (x, y)
head_coords = [0, 0]
tail_coords = [0, 0]
heads = []
unique_tail = {tuple(tail_coords)}

for instruction in instructions:
    for steps in range(int(instruction[1])):
        # move the head
        if instruction[0] in ['L', 'R']:
            head_coords[0] += parse_move(instruction[0], True)  # x +/- 1
        if instruction[0] in ['U', 'D']:
            head_coords[1] += parse_move(instruction[0], False)  # y +/- 1

        # check if the tail is still touching the head
        touching_x = abs(head_coords[0] - tail_coords[0]) < 2
        touching_y = abs(head_coords[1] - tail_coords[1]) < 2

        # adjust tail position
        if not touching_x:
            if head_coords[0] - tail_coords[0] > 1:
                tail_coords[0] += 1
            elif head_coords[0] - tail_coords[0] < -1:
                tail_coords[0] -= 1

        if not touching_y:
            if head_coords[1] - tail_coords[1] > 1:
                tail_coords[1] += 1
            elif head_coords[1] - tail_coords[1] < -1:
                tail_coords[1] -= 1

        unique_tail.add(tuple(tail_coords))
        # heads.append(tuple(head_coords))


print("Part 1:", len(unique_tail))
# print(heads)
print(unique_tail)
