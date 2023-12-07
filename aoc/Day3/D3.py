import re

from aoc.helper import AOCInputReader

from typing import List, Tuple

document_lines: list[str] = AOCInputReader.readLinesFromFile()


# sum of all of the part numbers in the engine schematic
def part_details():
    parts_details = []
    for line_index, line in enumerate(document_lines):
        matches = re.finditer("\\d+", line)
        for match in matches:
            print(f"Number {match.group()} found at index {match.start()}")
            number = match.group()
            number_index = match.start()
            is_part = is_engine_part(number, number_index, line_index, document_lines)
            print(f"{number}={is_part}")
            if is_part:
                parts_details.append((int(number), line_index, match.start(), match.end()))
    return parts_details


def is_symbol(s):
    return "." != s and not s.isalnum()


def is_engine_part(number: str, number_index, line_index_of_n, document_lines):
    has_neighbour = False
    line_n = document_lines[line_index_of_n]
    number_index_start = number_index
    number_index_end = number_index_start + len(number) - 1

    check_above = line_index_of_n > 0
    check_below = line_index_of_n < len(document_lines) - 1
    check_left = number_index_start > 0
    check_right = number_index_end < len(line_n) - 1

    index_left_neighbour = number_index_start - 1
    index_right_neighbour = number_index_end + 1
    if check_left and is_symbol(line_n[index_left_neighbour]):
        return True
    if check_right and is_symbol(line_n[index_right_neighbour]):
        return True

    start_index = index_left_neighbour if check_left else number_index_start
    end_index = index_right_neighbour if check_right else number_index_end
    document_line = None
    if check_above:
        document_line = document_lines[line_index_of_n - 1]
        for char in document_line[start_index:end_index + 1]:
            if is_symbol(char):
                return True
    if check_below:
        document_line = document_lines[line_index_of_n + 1]
        for char in document_line[start_index:end_index + 1]:
            if is_symbol(char):
                return True
    return False


def is_neighbour(a_start, a_length, b_start_index, b_length, offset=1):
    set1 = set(range(a_start - offset, a_start + a_length + offset))
    set2 = set(range(b_start_index, b_start_index + b_length))
    return len(set1.intersection(set2))


# expects a list of 3-tuple (number, line_index, start_index)
def gears(part_details: List[Tuple[int, int, int, int]]):
    sum = 0
    for i, line in enumerate(document_lines):
        for asterisk in re.finditer("\*", line):
            neighbours = 0
            values = []
            # only thos above,in, and below line
            number_start = [(number, index, start_index, end_index) for (number, index, start_index, end_index) in
                            part_details if
                            index in (i, i - 1, i + 1)]
            for number, index, start_index, end_index in number_start:
                if is_neighbour(asterisk.start(), 1, start_index, len(str(number))):
                    values.append(number)
            if len(values) == 2:
                sum = sum + (values[0] * values[1])
    return sum


if __name__ == '__main__':
    parts = [detail[0] for detail in part_details()]
    print(sum(parts))
    part_indices = [(number, line_index, start_index, end_index) for number, line_index, start_index, end_index in
                    part_details()]
    print(gears(part_indices))
