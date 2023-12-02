numbers_as_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers_as_digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def find_all_indexes(main_string, substring):
    indexes = [i for i in range(len(main_string)) if main_string.startswith(substring, i)]
    return indexes


def find_numbers(line: str):
    numbers_found = []  # list of tuples (the number, the index)
    for i in range(len(numbers_as_words)):
        num_as_word = numbers_as_words[i]
        word_indexes = find_all_indexes(line, num_as_word)
        num_word_as_digit = numbers_as_digits[i]
        for word_index in word_indexes:
            numbers_found.append((num_word_as_digit, word_index))

        digit = numbers_as_digits[i]
        digit_indexes = find_all_indexes(line, digit)
        for digit_index in digit_indexes:
            numbers_found.append((digit, digit_index))
    return numbers_found


def parse_input(input_text):
    sum_from_input = 0
    for line in input_text:
        numbers_found = find_numbers(line)
        sorted_list = sorted(numbers_found, key=lambda x: x[1])
        if len(sorted_list) > 1:
            first = sorted_list[0][0]
            second = sorted_list[len(sorted_list) - 1][0]
            num_from_line = f"{first}{second}"
        else:
            first = sorted_list[0][0]
            num_from_line = f"{first}{first}"
        sum_from_input += int(num_from_line)
    return sum_from_input


def main():
    #file_name = "p2-test"
    file_name = "puzzle"
    with open(file_name, 'r') as file:
        lines = file.readlines()
    input_text = []
    for line in lines:
        input_text.append(line.strip())

    sum_from_input = parse_input(input_text)
    print(sum_from_input)


main()
