"""
You are not required to write tests for this question.

The autograder for this question checks only two things:
1. There is not a file called "user_agent.txt"
2. The contents of "q1_contents.txt" match what we expect from that URL
"""

import json
import os
import sys
sys.path.append('.')

class TestWeatherURL:
    """Tests for the WeatherURL class"""

    def test_no_user_agent_file(self) -> None:
        """
        Test that there is no file called "user_agent.txt"
        """
        assert not os.path.exists('user_agent.txt')

    def test_q1_contents(self) -> None:
        """
        Test that the contents of "q1_contents.txt" match what we expect from the URL
        """
        with open('src/q1_contents.txt', 'r', encoding='utf-8') as f:
            contents = json.loads(f.read().strip())
        assert '@context' in contents
        assert 'properties' in contents
        assert 'geometry' in contents
