def find_start_marker(datastream, header_size):
    for chars_processed in range(header_size, len(datastream)):
        if len(set(datastream[chars_processed-header_size:chars_processed])) == header_size:
            return chars_processed


if __name__ == "__main__":
    with open("../inputs/day6.txt") as file:
        input_datastream = file.readline()
    print(f"Part 1: {find_start_marker(input_datastream, 4)}\nPart 2: {find_start_marker(input_datastream, 14)}")
