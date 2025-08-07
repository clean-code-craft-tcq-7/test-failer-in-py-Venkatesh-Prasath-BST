from misaligned import print_color_map, color_index_pair_number, add_post_space
import pytest


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