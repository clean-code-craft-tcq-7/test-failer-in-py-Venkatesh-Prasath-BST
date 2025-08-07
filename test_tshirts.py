import pytest
from tshirts import size


def test_tshirt_size():
    assert (size(37) == 'S')
    assert (size(38) == 'M')
    assert (size(40) == 'M')
    assert (size(43) == 'L')
    assert (size(5) == 'Invalid size')
    assert (size(50) == 'Invalid size')
    assert (size(100) == 'Invalid size')


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
    print("All is well (maybe!)")
