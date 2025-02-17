from src.mock.mock_examples import get_weather


def test_get_weather():
    """
    Test actual API call with default coordinates (Singapore)
    """
    response = get_weather()
    assert isinstance(response, dict)
    assert "current" in response
    assert "temperature_2m" in response["current"]


def test_get_weather_mocked(mocker):
    """Test get_weather with mocked API response"""
    mock_weather_data = {
        "latitude": 1.3521,
        "longitude": 103.8198,
        "timezone": "Asia/Singapore",
        "current": {
            "time": "2024-12-30T14:00",
            "temperature_2m": 25.6,
            "relative_humidity_2m": 80,
            "wind_speed_10m": 3.6,
        },
    }

    # Create a mock response object with a .json() method that returns the mock data
    mock_response = mocker.MagicMock()
    mock_response.json.return_value = mock_weather_data
    mock_response.raise_for_status.return_value = None

    # Patch 'requests.get' to return the mock response
    mocker.patch("requests.get", return_value=mock_response)

    # Call the function
    result = get_weather()

    assert isinstance(result, dict)
    assert "current" in result
    assert isinstance(result["current"]["temperature_2m"], (int, float))
    assert isinstance(result["current"]["wind_speed_10m"], (int, float))
    assert 0 <= result["current"]["relative_humidity_2m"] <= 100
    assert result["timezone"] == "Asia/Singapore"
