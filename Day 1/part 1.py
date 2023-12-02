def parse_input(input_text):
    stripped_lines = []
    for line in input_text:
        stripped_lines.append(line.strip())
    num_from_lines = []
    for line in stripped_lines:
        first = None
        second = None
        for char in line:
            try:
                int_char = int(char)
                if first is None:
                    first = int_char
                else:
                    second = int_char
            except:
                continue

        if second is not None:
            num_from_line = f"{first}{second}"
        else:
            num_from_line = f"{first}{first}"
        num_from_lines.append(num_from_line)
    sum = 0
    for num in num_from_lines:
        sum += int(num)
    return sum


def main():
    file_name = "puzzle"
    with open(file_name, 'r') as file:
        input_text = file.readlines()
    sum = parse_input(input_text)
    print(sum)


main()
