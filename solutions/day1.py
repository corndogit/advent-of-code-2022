# Golfed solution:
with open("../inputs/day1.txt") as file:
    meals = list(map(lambda x: list(map(lambda y: int(y if len(y) > 0 else 0), x.split('\n'))), file.read().split('\n\n')))
    print("Part 1: Most calories carried by a single elf =", max(map(sum, [m for m in meals])))
    print("Part 2: Total calories counted by top 3 elves =", sum(sorted(map(sum, [m for m in meals]), reverse=True)[:3]))


# First attempt:
meals = []
with open("../inputs/day1.txt") as file:
    for f in file.readlines():
        meal = f.strip('\n')
        meals.append(int(meal) if len(meal) > 0 else 0)

elves = []
current_calories = 0
for m in meals:
    if m > 0:
        current_calories += m
    else:
        elves.append(current_calories)
        current_calories = 0

print("Part 1: Most calories carried by a single elf =", max(elves))

print("Part 2: Total calories counted by top 3 elves =", sum(sorted(elves)[::-1][:3]))
