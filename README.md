# real-time-weather-
# Real-Time Weather Info & Logger
# Overview
This Python application fetches real-time weather data from OpenWeatherMap API for user-specified cities and logs all responses with timestamps to both SQLite database and text files .Designed with Object-Oriented Programming (OOP) principles to keep code organized and maintainable. Proper error handling ensures robustness against invalid city names or API issues.

# Project Structure
WEATHER ├── config.py ├── requirements.txt ├── weather_client.py └── db_manager.py ├── main.py ├── utils.py

 # Features
Input city names interactively or type exit to quit.

Fetches live temperature (in °C), humidity (%), and weather conditions.

Displays simple meaningful explanations about temperature and humidity values.

Logs each lookup response into a SQLite database with a timestamp.

Uses OOP with clear separation of concerns: fetching data, displaying info, and logging.

Handles invalid inputs and API errors gracefully.

# Requirements
```
Python 3.6+
```
requests library

# Installation

1.Clone or download the project files

2.Install required dependencies:

```
pip install requests
```

3.Get an API key from OpenWeatherMap Sign up for a free account Generate an API key in your dashboard
