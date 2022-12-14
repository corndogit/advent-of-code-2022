def part1(section_ids):
    set_a = set(range(section_ids[0], section_ids[1] + 1))
    set_b = set(range(section_ids[2], section_ids[3] + 1))
    smallest_set = set_a if len(set_a) < len(set_b) else set_b
    return set_a & set_b == smallest_set


def part2(section_ids):
    set_a = set(range(section_ids[0], section_ids[1] + 1))
    set_b = set(range(section_ids[2], section_ids[3] + 1))
    return not len(set_a & set_b) == 0


with open("../inputs/day4.txt") as file:
    sections = list(map(lambda s: list(map(int, s)),
                        [ids.replace('-', ',').split(',') for ids in file.read().splitlines()]))

print("Part 1:", len(list(filter(part1, sections))))
print("Part 2:", len(list(filter(part2, sections))))
