import re

import AOCInputReader

document_lines = AOCInputReader.readLinesFromFile()



# sum of all of the part numbers in the engine schematic
def sum_part_numbers_in_engine():

    parts = []
    for line_index, line in enumerate(document_lines):
        matches = re.finditer("\\d+", line)
        for match in matches:
            print(f"Number {match.group()} found at index {match.start()}")
            number = match.group()
            number_index = match.start()
            is_part = is_engine_part(number, number_index, line_index, document_lines)
            print(f"{number}={is_part}")
            if is_part:
                parts.append(int(number))
    return parts


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

def gears():


    return

if __name__ == '__main__':
    parts = sum_part_numbers_in_engine()
    sum(parts)
    gears()