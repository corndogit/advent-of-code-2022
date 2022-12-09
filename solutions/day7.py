import re
import json


class Directory:
    def __init__(self, path: str, size: int):
        self.path = path
        self.size = size

    def __repr__(self):
        return f"path: {self.path}, size: {self.size}"

    def add_to_size(self, value: int):
        self.size += value


def check_key_exists(path):
    if not ''.join(path) in file_system.keys():
        file_system[''.join(path)] = []


def sum_of_subdirectories(directories: list[Directory]):
    sums = []
    for d in directories:
        if len(sums) == 0:
            sums.append(d)
        elif sums[-1].path in d.path and len(sums[-1].path) > 1:
            sums[-1].add_to_size(d.size)
            sums.append(d)
        else:
            sums.append(d)

    return sum([s.size for s in sums])


with open("../inputs/day7.txt") as file:
    history = [line.split(' ') for line in file.read().splitlines()]

file_system = {}
current_path = ['/']
check_key_exists(current_path)

for cmd in history:
    # cd commands
    if cmd[0:2] == ['$', 'cd']:
        if cmd[-1] == '/':
            current_path = ['/']
        elif cmd[-1] == '..':
            current_path.pop(-1)
        else:
            current_path.append(f"{cmd[-1]}/")

    # dirs
    if cmd[0] == 'dir':
        check_key_exists(current_path + [cmd[1] + "/"])

    # files
    if re.match(r'\d+', cmd[0]):
        file_system[''.join(current_path)].append({"filename": cmd[1], "size": int(cmd[0])})

# print out the file system
print(json.dumps(file_system, indent=2))

# get size of each directory in the file system
directory_sizes = []
for keys, values in zip(file_system.keys(), file_system.values()):
    if len(values) > 0:
        directory = Directory(keys, values[0]['size'])
        for files in values[1:]:
            directory.add_to_size(files['size'])
        directory_sizes.append(directory)

directories_above_100000 = list(filter(lambda f: f.size < 100_000, directory_sizes))
print(directories_above_100000)
print("Part 1:", sum_of_subdirectories(directories_above_100000))
