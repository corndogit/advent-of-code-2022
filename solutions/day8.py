def find_trees_in_straight_line(trees, x, y):
    """
    Find the largest trees in a straight line in each direction from current (excluding self)
    :param trees: Puzzle input
    :param x: Index of tree in row
    :param y: Index of row
    :return: Tuple of lists containing each tree direction clockwise from current
    """
    tree_up = list(reversed([trees[col][x] for col in range(y)]))
    tree_right = trees[y][x + 1:]
    tree_down = [trees[col][x] for col in range(y + 1, len(trees))]
    tree_left = list(reversed(trees[y][:x]))

    return tree_up, tree_right, tree_down, tree_left


def find_distance(tree_line, limit):
    """
    Counts how many trees are in a line from the current tree before reaching one at the height limit
    :param tree_line: trees in a direction
    :param limit: height limit to stop counting at
    :return: distance between current tree and a tree at the height limit
    """
    distance = 0
    for tree in tree_line:
        distance += 1
        if tree >= limit:
            return distance

    return distance


def part_1(trees):
    """
    Count how many trees are visible from outside the grid.
    :param trees: Puzzle input
    :return: Number of visible trees
    """
    visible_trees = 4 * (len(trees[0]) - 2) + 4  # number of trees on the edge

    for y in range(1, len(trees) - 1):
        for x in range(1, len(trees[0]) - 1):
            current_tree = trees[y][x]
            surrounding_trees_max = map(max, find_trees_in_straight_line(trees, x, y))

            tree_is_visible = list(filter(lambda tree: current_tree > tree, surrounding_trees_max))
            if len(tree_is_visible) > 0:
                visible_trees += 1

    return visible_trees


def part_2(trees):
    """
    Find the highest possible scenic score for the trees
    :param trees: Puzzle input
    :return: The highest scenic score value
    """
    highest_score = 0
    for y in range(1, len(trees) - 1):
        for x in range(1, len(trees[0]) - 1):
            score = 1
            current_tree = trees[y][x]
            surrounding_trees = find_trees_in_straight_line(trees, x, y)
            for direction in surrounding_trees:
                distance = find_distance(direction, current_tree)
                score = score * distance
            if score > highest_score:
                highest_score = score
    return highest_score


if __name__ == "__main__":
    with open("../inputs/day8.txt") as file:
        puzzle_input = [[int(r) for r in row] for row in file.read().splitlines()]

    print("Part 1", part_1(puzzle_input))
    print("Part 2", part_2(puzzle_input))
