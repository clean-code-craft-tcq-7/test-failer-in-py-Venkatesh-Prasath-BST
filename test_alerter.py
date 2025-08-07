import pytest
from alerter import alert_in_celcius, network_alert_stub, alert_failure_count


def test_alert_in_celcius():
    # Reset the failure count before testing
    import alerter
    alerter.alert_failure_count = 0
    
    # Test with various temperatures
    alert_in_celcius(400)
    alert_in_celcius(200)
    alert_in_celcius(500)
    alert_in_celcius(150)
    alert_in_celcius(250)
    
    # Check that alert_failure_count is not zero
    # This test will fail because the bug in alerter.py increments by 0 instead of 1
    assert alerter.alert_failure_count != 0, "Expected some alerts to fail, but failure count is zero"


def test_netwrok_alert_stub():
    # yet to get the requirements for this function
    pass


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
    print("All is well (maybe!)")
