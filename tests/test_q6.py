"""HW6 Question 6 Tests

You only need to add tests for WeatherAPIError. Tests for WeatherForcast are provided.
"""

import sys
from unittest import mock
import pandas as pd
sys.path.append('.')
from src.q6 import WeatherForecast, WeatherAPIError

class TestWeatherForecast:
    """Tests for the WeatherForecast class"""

    def test_get_weather_calls_get_weather_url(self) -> None:
        """Tests that WeatherForecast.get_weather() calls WeatherURL.get_weather_url() 
        with the correct arguments"""
        wf = WeatherForecast('tests/_user_agent.txt')
        with mock.patch('src.q5.WeatherURL.get_weather_url') as mock_get_weather_url:
            mock_get_weather_url.return_value = \
                'https://api.weather.gov/gridpoints/MTR/90,105/forecast'
            with mock.patch('requests.get') as mock_requests_get:
                mock_response = mock.Mock()
                mock_response.json.return_value = {
                    'properties': {
                        'periods': []
                    }
                }
                mock_requests_get.return_value = mock_response
                wf.get_weather(1.3, -2.4)
                mock_get_weather_url.assert_called_with(1.3, -2.4)

    def test_get_weather_has_columns(self) -> None:
        """Tests that the dataframe returned by WeatherForecast.get_weather() 
        has the correct columns and types"""
        wf = WeatherForecast('tests/_user_agent.txt')
        df = wf.get_weather()
        assert isinstance(df, pd.DataFrame)
        assert 'startTime' in df.columns
        assert 'endTime' in df.columns
        assert 'temperature' in df.columns
        assert 'probabilityOfPrecipitation' in df.columns
