def get_cube_count_and_colour(cube_color_and_count: str):
    if "blue" in cube_color_and_count:
        cube_count = cube_color_and_count.replace(" blue", "")
        return cube_count, "blue"
    elif "green" in cube_color_and_count:
        cube_count = cube_color_and_count.replace(" green", "")
        return cube_count, "green"
    else:
        cube_count = cube_color_and_count.replace(" red", "")
        return cube_count, "red"


def parse_input(input_text):
    powers = []
    for game in input_text:
        min_blue = 0
        min_green = 0
        min_red = 0

        all_cube_subsets: str = game.split(':')[1]
        cube_subset_list = all_cube_subsets.split(';')
        for subset in cube_subset_list:
            cube_count_and_colors = subset.split(',')
            for cube in cube_count_and_colors:
                cube_count, cube_colour = get_cube_count_and_colour(cube.strip())
                if cube_colour == "blue" and int(cube_count) > min_blue:
                    min_blue = int(cube_count)
                elif cube_colour == "green" and int(cube_count) > min_green:
                    min_green = int(cube_count)
                elif cube_colour == "red" and int(cube_count) > min_red:
                    min_red = int(cube_count)
        game_power = min_red * min_green * min_blue
        powers.append(game_power)
    power_sum = 0
    for power in powers:
        power_sum += power
    return power_sum


def main():
    file_name = "puzzle"
    with open(file_name, 'r') as file:
        input_text = file.readlines()
    game_id_sum = parse_input(input_text)
    print(game_id_sum)


main()
