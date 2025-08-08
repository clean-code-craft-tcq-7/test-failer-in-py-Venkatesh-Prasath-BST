
def color_index_pair_number(major_color_index, minor_color_index):
    return major_color_index * 5 + minor_color_index + 1


def __number_of_characters_in_largest_value_in_list(input_list):
    return max(len(str(item)) for item in input_list)


def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    major_color_max_char = __number_of_characters_in_largest_value_in_list(major_colors)
    minor_color_max_char = __number_of_characters_in_largest_value_in_list(minor_colors)
    for i, major in enumerate(major_colors):
        dashes_for_major = '-' * (major_color_max_char)
        dashes_for_minor = '-' * (minor_color_max_char)
        print(f"| -- | {dashes_for_major} | {dashes_for_minor} |")
        for j, minor in enumerate(minor_colors):
            index_num = color_index_pair_number(i, j)
            print(f'| {index_num:<2} | {major:<{major_color_max_char}} | {minor:<{minor_color_max_char}} |')
    print(f"| -- | {dashes_for_major} | {dashes_for_minor} |")
    return len(major_colors) * len(minor_colors)


if __name__ == '__main__':  # pragma: no cover
    print_color_map()
