MAX_BLUE = 14
MAX_GREEN = 13
MAX_RED = 12


def get_game_id(game_line):
    game_input: str = game_line.split(':')[0]
    return game_input.replace("Game ", "")


def valid_cube_count(cube_color_and_count: str):
    if "blue" in cube_color_and_count:
        cube_count = cube_color_and_count.replace(" blue", "")
        return int(cube_count) <= MAX_BLUE
    elif "green" in cube_color_and_count:
        cube_count = cube_color_and_count.replace(" green", "")
        return int(cube_count) <= MAX_GREEN
    else:
        cube_count = cube_color_and_count.replace(" red", "")
        return int(cube_count) <= MAX_RED


def parse_input(input_text):
    valid_game_ids = []
    for game in input_text:
        valid_game = True
        game_id = get_game_id(game)
        all_cube_subsets: str = game.split(':')[1]
        cube_subset_list = all_cube_subsets.split(';')
        for subset in cube_subset_list:
            cube_count_and_colors = subset.split(',')
            for cube in cube_count_and_colors:
                cube = cube.strip()
                if not valid_cube_count(cube):
                    valid_game = False
        if valid_game:
            valid_game_ids.append(game_id)
    game_id_sum = 0
    for game_id in valid_game_ids:
        game_id_sum += int(game_id)
    return game_id_sum


def main():
    file_name = "puzzle"
    with open(file_name, 'r') as file:
        input_text = file.readlines()
    game_id_sum = parse_input(input_text)
    print(game_id_sum)


main()
