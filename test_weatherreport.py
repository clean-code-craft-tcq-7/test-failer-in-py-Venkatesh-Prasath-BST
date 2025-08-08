import pytest
from weatherreport import report


def high_precipitation_stub():
    return {
        'temperature_inc': 25,
        'precipitation': 70,
        'humidity': 26,
        'wind_speed_kmph': 40
    }


def sensor_stub():
    return {
        'temperature_inc': 50,
        'precipitation': 70,
        'humidity': 26,
        'wind_speed_kmph': 52
    }


def test_rainy():
    weather = report(sensor_stub)
    print(weather)
    assert ("rain" in weather)


def test_high_precipitaion():
    # This instance of stub needs to be different-
    # to give high precipitation (>60) and low wind-speed (<50)

    weather = report(high_precipitation_stub)
    print(weather)

    # strengthen the assert to expose the bug
    # (function returns Sunny day, it should predict rain)
    assert ("rain" in weather)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
    print("All is well (maybe!)")
