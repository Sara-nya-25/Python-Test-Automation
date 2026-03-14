
class WeatherApp:
    def __init__(self, service):
        self.service = service

    def get_today_summary(self, city):
        data = self.service.get_city_weather(city)
        return f"Today in {city}: {data}"

    def is_it_icy(self, city):
        temp = self.service.get_temperature(city)
        return temp < 0