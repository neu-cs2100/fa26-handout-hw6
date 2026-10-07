"""HW6 Question 6: parsing JSON, raising a custom error

In this question, you will implement a method to retrieve and parse weather data from 
the National Weather Service API and return it as a Pandas dataframe. You will also raise
a custom error if the expected keys are not found in the API response.

Please create a custom error called a WeatherAPIError, which will be raised if the data returned
by the weather API does not contain the expected format.

Please also implement the `get_weather` method in the class below to fit the documentation.

You are not required to write tests for `get_weather`; they are provided for you.
You should still provide appropriate documentation and tests for the WeatherAPIError.
"""

import sys
from typing import Any
import requests
import pandas as pd
sys.path.append('.')
from src.q5 import WeatherURL


class WeatherForecast:
    """Retrieves the weather forecast from the National Weather Service"""

    def __init__(self, user_agent_file: str) -> None:
        """
        Instantiates the WeatherForecast object with the User Agent from the specified file
        
        Args:
            user_agent_file : str
                the file that contains the User Agent
        
        Raises:
            FileNotFoundError: if the specified user agent file does not exist
        """
        with open(user_agent_file, 'r', encoding='utf-8') as f:
            self._user_agent = f.read().strip()
    
    def get_weather(self, latitude: float = 38.9953, longitude: float = -77.0287) -> Any:
        """
        Return a dataframe containing the predicted temperatures and chances of precipitation,
        with timestamps.
        
        Args:
            latitude : float
                the latitude for which we want the weather
            longitude : float
                the longitude for which we want the weather
        
        Returns:
            A Pandas dataframe with the following columns:
                | startTime | endTime | temperature | probabilityOfPrecipitation |
                The temperature should be in Fahrenheit
        
        Raises:
            requests.exceptions.RequestException: if the request to the weather API fails
            WeatherAPIError: if the expected keys are not found in the API response
        """
        #TODO: use WeatherURL.get_weather_url() to get the URL for the weather
        #TODO: parse through the "periods" in the weather (in the "properties" section),
        #       and put the data into a Pandas dataframe of this format:
        #       | startTime | endTime | temperature | probabilityOfPrecipitation |
        #
        #       The columns in the dataframe should be named as specified above.
        #       The temperature should be in Fahrenheit.
