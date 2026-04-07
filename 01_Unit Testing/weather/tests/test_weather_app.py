import unittest
from unittest.mock import MagicMock
from src.weather_app import WeatherApp


class TestWeatherApp(unittest.TestCase):
    # TDD Cycle: User Story 1 (Search City)
    # Search Today's Weather: As a visitor, I want to search for my city, so I can see what the weather will be like today.
    def test_get_today_summary_returns_correct_string(self):
        # Setup: Mock the service
        mock_service = MagicMock()
        mock_service.get_city_weather.return_value = "Sunny, 22°C"

        app = WeatherApp(mock_service)
        result = app.get_today_summary("Stockholm")

        self.assertEqual(result, "Today in Stockholm: Sunny, 22°C")
        mock_service.get_city_weather.assert_called_with("Stockholm")

     # Temperature Alert: As a hiker, I want to know if it's below $0^\circ\text{C}$ in my city, so I know if the trails are icy.
    def test_is_it_icy_returns_true_when_below_zero(self):
        mock_service = MagicMock()
        # Mocking the service to return a numeric temperature
        mock_service.get_temperature.return_value = -5

        app = WeatherApp(mock_service)
        self.assertTrue(app.is_it_icy("Kiruna"))


if __name__ == '__main__':
    unittest.main()
