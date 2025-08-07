

def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    # proposed changes, the initial condition shall start with  precipitaion
    # instead of temperature
    if (readings['temperature_inc'] > 25):
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['wind_speed_kmph'] > 50:
            weather = "Alert, Stormy with heavy rain"
    return weather
