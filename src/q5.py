"""HW6 Question 5: using an API without exposing personal info

"API" stands for "Application Programming Interface". Programmers often use APIs to interact 
with external services and retrieve data programmatically. In the next two questions, you will
practice using an API.

The code for this question is already provided. It uses the free API provided by the National 
Weather Service: https://www.weather.gov/documentation/services-web-api

As you can see in their documentation, retrieving data from their API requires specifying
a "User-Agent": some information to identify you. (This way, the API provider knows who is 
making the request.) That information is not verified, which is probably why they plan to 
replace the User-Agent requirement with an API key soon.

For example, this is a valid User-Agent: 
Northeastern University Student (Contact: student@northeastern.edu)

Your task is to get this code to work by creating a file called "user_agent.txt", 
which contains your User-Agent info. However, you MUST NOT push the "user_agent.txt"
file to GitHub. It is sensitive personal information. (People pushing personal info to public 
repositories on GitHub can expose themselves to privacy risks.) You can do this by adding 
"user_agent.txt" to your ".gitignore" file, or simply not `git add`ing it.

If this code works, it will print a URL. Navigate to that URL in a browser, and copy
the contents of that page into q5_contents.txt. (Replace the text that is currently 
in the file.) It is weather info.

The autograder for this question checks only two things:
1. There is not a file called "user_agent.txt"
2. The contents of "q5_contents.txt" match what we expect from that URL
"""

from pprint import pprint
from typing import Any
import sys
import requests
sys.path.append('.')

class WeatherURL:
    """A class to get the URL for the weather forecast for a given latitude and longitude."""
    def __init__(self, user_agent: str) -> None:
        """
        Stores the provided User Agent
        
        Args:
            user_agent : str
                the User Agent
        """
        self._user_agent = user_agent

    def get_weather_url(self, latitude: float = 37.8049, longitude: float = -122.2725) -> Any:
        """
        Return the URL at which we can find the weather forecase for the provided latitude 
        and longitude.

        Args:
            latitude : float
                the latitude for which we want the weather URL
            longitude : float
                the longitude for which we want the weather URL
        
        Return:
            str / Any: the URL at which we can find the weather forecast 
                    (if the request was successful and formatted correctly)
        
        Raises:
            KeyError: if the request was not successful
        """
        headers = {'User-Agent': self._user_agent}
        url = f'https://api.weather.gov/points/{latitude},{longitude}'
        request = requests.get(url, headers=headers, timeout=10)
        request.raise_for_status()
        data = request.json()
        if 'properties' not in data or 'forecast' not in data.get('properties'):
            raise KeyError('Response JSON does not contain expected keys')
        return data.get('properties').get('forecast')

if __name__ == '__main__':
    with open('user_agent.txt', 'r', encoding='utf-8') as f:
        user_agent_from_file = f.read().strip()
    weather_agent = WeatherURL(user_agent_from_file)
    weather = weather_agent.get_weather_url()
    pprint(weather)
