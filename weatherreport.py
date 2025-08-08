

def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if readings['precipitation'] > 0:
        weather = "rainy day"
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "raining and partly cloudy"
        elif readings['wind_speed_kmph'] > 50:
            weather = "Alert, Stormy with heavy rain"
    return weather
