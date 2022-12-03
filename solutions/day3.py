from string import ascii_letters

# create item priority dict
priorities = {char: num for num, char in enumerate(ascii_letters, 1)}


def common_items(bag: list[str]):
    common = 0
    for item in bag[0]:
        if item in bag[1]:
            common = priorities[item]

    return common


if __name__ == "__main__":
    bags = []
    with open("../inputs/day3.txt") as file:
        # split bags into their two compartments
        for bag in file.readlines():
            mid = int(len(bag.strip('\n')) / 2)  # midpoint where the bags separate into compartments
            bags.append([bag[:mid], bag.strip('\n')[-mid:]])

    # convert every bag in bags into a set
    bag_sets = list(map(lambda b: set("".join(b)), bags))

    # find the priority of the common item for every group of 3 bags
    group_priorities = [priorities[max(bag_sets[i].intersection(bag_sets[i + 1], bag_sets[i + 2]))]
                        for i in range(0, len(bags), 3)]

    print("part1:", sum(map(common_items, bags)))
    print("part2:", sum(group_priorities))
