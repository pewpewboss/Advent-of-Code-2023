from aoc.helper import AOCInputReader

alphas = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
digits = (1, 2, 3, 4, 5, 6, 7, 8, 9)


# returns the first number found as a string (e.g. "1", "one", "two, "three", "nine"
def find_first_number_string(calibration: str):
    alpha_indices = []
    digit_indices = []
    for alpha, digit in zip(alphas, digits):
        alpha_index = calibration.find(alpha)
        if alpha_index != -1:
            alpha_indices.append((alpha_index, alpha))
        digit_index = calibration.find(str(digit))
        if digit_index != -1:
            digit_indices.append((digit_index, str(digit)))
    print(f"alpha_indices {alpha_indices}")
    print(f"digit_indices {digit_indices}")
    min_tuple_alphas = min(alpha_indices, default=None, key=lambda tup: tup[0])
    print(f" min_tuple_alphas {min_tuple_alphas}")
    min_tuple_digits = min(digit_indices, default=None, key=lambda tup: tup[0])
    print(f" min_tuple_digits {min_tuple_digits}")
    real_first = ""
    if min_tuple_alphas is None:
        real_first = min_tuple_digits[1]
    elif min_tuple_digits is None:
        real_first = min_tuple_alphas[1]
    else:
        real_first = min(min_tuple_digits, min_tuple_alphas)[1]
    print(f"real_first: {real_first}")
    return real_first


# returns the last number found as a string (e.g. "1", "one", "two, "three", "nine"
def find_last_number_string(string):
    alpha_indices = []
    digit_indices = []
    for alpha, digit in zip(alphas, digits):
        alpha_index = string.rfind(alpha)
        if alpha_index != -1:
            alpha_indices.append((alpha_index, alpha))
        digit_index = string.rfind(str(digit))
        if digit_index != -1:
            digit_indices.append((digit_index, str(digit)))
    min_tuple_alphas = max(alpha_indices, default=None, key=lambda tup: tup[0])
    min_tuple_digits = max(digit_indices, default=None, key=lambda tup: tup[0])
    real_last = ""
    if min_tuple_alphas is None:
        real_last = min_tuple_digits[1]
    elif min_tuple_digits is None:
        real_last = min_tuple_alphas[1]
    else:
        real_last = max(min_tuple_digits, min_tuple_alphas)[1]
    print(f"real_last: {real_last}")
    return real_last


def combine_to_int(x: str, y: str):
    alpha_to_digits = dict(zip(alphas, digits))
    #   "1" and "2"
    if x.isdigit() and y.isdigit():
        combined = x + y  # "1" and "2" -> "12"
        return int(combined)  # 12
    #   "one" and "two"
    if x.isalpha() and y.isalpha():
        combined = str(alpha_to_digits.get(x)) + str(alpha_to_digits.get(y))  # "1" and "2" -> "12"
        return int(combined)  # 12
    #   "1" and "two"
    if x.isdigit() and y.isalpha():
        combined = x + str(alpha_to_digits.get(y))  # "1" and "2" -> "12"
        return int(combined)  # 12
    #   "one" and "2"
    if x.isalpha() and y.isdigit():
        combined = str(alpha_to_digits.get(x)) + y  # "1" and "2" -> "12"
        return int(combined)


def part2(lines):
    all_callibrations = []
    for calibration in lines:
        first_number = find_first_number_string(calibration)
        last_number = find_last_number_string(calibration)
        calibration_value = combine_to_int(first_number, last_number)
        # add the combined number e.g. 7 + six as 76
        all_callibrations.append(calibration_value)
        print(f"calibration_value: {calibration_value}")
    sum_all = sum(all_callibrations)
    print(f"sum of all: {sum_all}")


def part1(lines):
    document = []
    for line in lines:
        numbers = list(filter(lambda x: x.isdigit(), line))
        document.append((numbers[0], numbers[-1]))
    print(document)
    total = 0
    for x, y in document:
        string = str(x + y)
        total += (int(string))
    print(total)


if __name__ == '__main__':
    calibration_document = AOCInputReader.readLinesFromFile("input.txt")
    #part1(calibration_document)
    part2(calibration_document)

