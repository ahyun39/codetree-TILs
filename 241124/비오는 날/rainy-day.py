class Weather:
    def __init__(self, date, day, weather_predict):
        self.date = date
        self.day = day
        self.predict = weather_predict

hows_the_weather = [list(map(str, input().split())) for _ in range(int(input()))]

hows_the_weather.sort(key=lambda x:x[0])

for htw in hows_the_weather:
    if htw[2] == "Rain":
        weather = Weather(htw[0], htw[1], htw[2])
        break

print(weather.date, weather.day, weather.predict)
    