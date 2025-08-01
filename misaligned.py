import pytest


def color_index_pair_number(major_color_index, minor_color_index):
    if major_color_index < 0 or minor_color_index < 0:
        raise ValueError("Indices must be non-negative")
    return major_color_index * 5 + minor_color_index + 1


def __number_of_characters_in_largest_value_in_list(input_list):
    if not input_list:
        return 0
    return max(len(str(item)) for item in input_list)


def add_post_space(input_string, max_length):
    if len(input_string) >= max_length:
        return input_string
    return input_string + ' ' * (max_length - len(input_string))


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
            index_num_with_space = add_post_space(str(index_num), 2)
            major_with_space = add_post_space(major, major_color_max_char)
            minor_with_space = add_post_space(minor, minor_color_max_char)
            print(f'| {index_num_with_space} | {major_with_space} | {minor_with_space} |')
    print(f"| -- | {dashes_for_major} | {dashes_for_minor} |")
    return len(major_colors) * len(minor_colors)


# ------------- TESTS ------------- #
def test_print_color_map():
    assert(print_color_map() == 25)


def test_color_index_pair_number():
    assert(color_index_pair_number(0, 0) == 1)
    assert(color_index_pair_number(4, 4) == 25)
    assert(color_index_pair_number(2, 3) == 14)
    assert(color_index_pair_number(4, 1) == 22)


def test_add_post_space():
    assert(add_post_space("Hello", 10) == "Hello     ")
    assert(add_post_space("World", 5) == "World")
    assert(add_post_space("", 5) == "     ")
    assert(add_post_space("Test", 8) == "Test    ")


if __name__ == '__main__':
    print_color_map()
    pytest.main([__file__, '-v'])
    print("All is well (maybe!)")
