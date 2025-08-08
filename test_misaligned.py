from misaligned import print_color_map, color_index_pair_number
import pytest


def test_print_color_map():
    assert (print_color_map() == 25)


def test_color_index_pair_number():
    assert (color_index_pair_number(0, 0) == 1)
    assert (color_index_pair_number(4, 4) == 25)
    assert (color_index_pair_number(2, 3) == 14)
    assert (color_index_pair_number(4, 1) == 22)


if __name__ == '__main__':
    print_color_map()
    pytest.main([__file__, '-v'])
    print("All is well (maybe!)")
