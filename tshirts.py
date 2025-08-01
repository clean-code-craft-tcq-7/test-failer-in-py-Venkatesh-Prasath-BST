import pytest


def size(cms):
    size_map = {
        range(35, 38): 'S',
        range(38, 42): 'M',
        range(42, 47): 'L'
    }
    
    for size_range, size_label in size_map.items():
        if cms in size_range:
            return size_label
    
    return 'Invalid size'


def test_tshirt_size():
    assert(size(37) == 'S')
    assert(size(38) == 'M')
    assert(size(40) == 'M')
    assert(size(43) == 'L')
    assert(size(5) == 'Invalid size')
    assert(size(50) == 'Invalid size')
    assert(size(100) == 'Invalid size')


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
    print("All is well (maybe!)")
