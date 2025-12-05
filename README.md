# Real-Time Weather Info & Logger
# Overview
This Python application fetches real-time weather data from OpenWeatherMap API for user-specified cities and logs all responses with timestamps to both SQLite database and text files .Designed with Object-Oriented Programming (OOP) principles to keep code organized and maintainable. Proper error handling ensures robustness against invalid city names or API issues.

# Project Structure
WEATHER ├── config.py ├── requirements.txt ├── weather_client.py └── db_manager.py ├── main.py ├── utils.py

 # Features
-  Input city names interactively or type exit to quit.
-  Fetches live temperature (in °C), humidity (%), and weather conditions.
-  Displays simple meaningful explanations about temperature and humidity values.
-  Logs each lookup response into a SQLite database with a timestamp.
-  Uses OOP with clear separation of concerns: fetching data, displaying info, and logging.
-  Handles invalid inputs and API errors gracefully.

# Requirements
-  Python 3.6+
-  Requests library

# Installation

1.Clone or download the project files

2.Install required dependencies:

```
pip install requests
```

3.Get an API key from OpenWeatherMap Sign up for a free account Generate an API key in your dashboard
data Storage & Logging
# SQLite Database: 

-  All API responses are automatically logged with timestamps
-  Persistent Storage: Data remains available between sessions
-  Structured Logging: Each entry includes:
-  Timestamp of request
-  City name searched
# Database Schema
The SQLite database weather_logs.db contains one table named weather_data with the following fields:
```

Column  Type  Description

id INTEGER  Auto-increment primary key

city  TEXT  Name of the city

temperature REAL Temperature in Celsius

humidity INTEGER Humidity percentage

conditions TEXT	Weather condition description (e.g., clear sky)

timestamp TEXT  Date and time when data was logged
```
# Error Handling

-  If the city name is empty, the program prompts for a valid name.
-  If the API request fails (network issues or invalid city), an error message is displayed.
-  Unexpected API response formats are caught and notified to the user.
-  Database connection problems.
# Example
```
========= Weather Application =========
1. Get weather for a city
2. View all weather logs
3. View statistics
4. Clear all logs
5. Exit

Enter your choice: 1
Enter city name: ponnur
==================================================
City         : Ponnur
Temperature  : 29.98 °C
Humidity     : 69 %
Pressure     : 1012 hPa
Wind Speed   : 2.64 m/s
Condition    : overcast clouds
Timestamp    : 2025-12-04 15:48:21
==================================================

========= Weather Application =========
1. Get weather for a city
2. View all weather logs
3. View statistics
4. Clear all logs
5. Exit

Enter your choice: 1
Enter city name: nellore
==================================================
City         : Nellore
Temperature  : 26.89 °C
Humidity     : 76 %
Pressure     : 1012 hPa
Wind Speed   : 6.02 m/s
Condition    : light rain
Timestamp    : 2025-12-04 15:48:34
==================================================

========= Weather Application =========
1. Get weather for a city
2. View all weather logs
3. View statistics
4. Clear all logs
5. Exit

Enter your choice: 1
Enter city name: ongole
==================================================
City         : Ongole
Temperature  : 25.51 °C
Humidity     : 81 %
Pressure     : 1013 hPa
Wind Speed   : 5.09 m/s
Condition    : overcast clouds
Timestamp    : 2025-12-04 15:48:43
==================================================

========= Weather Application =========
1. Get weather for a city
2. View all weather logs
3. View statistics
4. Clear all logs
5. Exit

Enter your choice: 1
Enter city name: tirupati
==================================================
City         : Tirupati
Temperature  : 24.57 °C
Humidity     : 94 %
Pressure     : 1013 hPa
Wind Speed   : 2.06 m/s
Condition    : mist
Timestamp    : 2025-12-04 15:48:51
==================================================

========= Weather Application =========
1. Get weather for a city
2. View all weather logs
3. View statistics
4. Clear all logs
5. Exit

Enter your choice: 1 
Enter city name: kochi
==================================================
City         : Kochi
Temperature  : 29.95 °C
Humidity     : 70 %
Pressure     : 1010 hPa
Wind Speed   : 4.02 m/s
Condition    : broken clouds
Timestamp    : 2025-12-04 15:49:05
==================================================

========= Weather Application =========
1. Get weather for a city
2. View all weather logs
3. View statistics
4. Clear all logs
5. Exit

Enter your choice: 1
Enter city name: goa
==================================================
City         : Goa
Temperature  : 32.21 °C
Humidity     : 46 %
Pressure     : 1009 hPa
Wind Speed   : 4.43 m/s
Condition    : broken clouds
Timestamp    : 2025-12-04 15:49:14
==================================================

========= Weather Application =========
1. Get weather for a city
2. View all weather logs
3. View statistics
4. Clear all logs
5. Exit

Enter your choice: 2
==================================================
(2, 'Ponnur', 29.98, 69.0, 1012.0, 2.64, 'overcast clouds', '2025-12-04 15:48:21')
(3, 'Nellore', 26.89, 76.0, 1012.0, 6.02, 'light rain', '2025-12-04 15:48:34')
(4, 'Ongole', 25.51, 81.0, 1013.0, 5.09, 'overcast clouds', '2025-12-04 15:48:43')
(5, 'Tirupati', 24.57, 94.0, 1013.0, 2.06, 'mist', '2025-12-04 15:48:51')
(6, 'Kochi', 29.95, 70.0, 1010.0, 4.02, 'broken clouds', '2025-12-04 15:49:05')
(7, 'Goa', 32.21, 46.0, 1009.0, 4.43, 'broken clouds', '2025-12-04 15:49:14')
==================================================

========= Weather Application =========
1. Get weather for a city
2. View all weather logs
3. View statistics
4. Clear all logs
5. Exit

Enter your choice: 3
==================================================
Average Temperature: 28.185000000000002
Average Humidity   : 72.66666666666667
Average Humidity   : 72.66666666666667  
Average Pressure   : 1011.5
Average Humidity   : 72.66666666666667  
Average Humidity   : 72.66666666666667  
Average Pressure   : 1011.5
========================================Average Humidity   : 72.66666666666667  
Average Humidity   : 72.66666666666667
Average Pressure   : 1011.5
==================================================

========= Weather Application =========
1. Get weather for a city
2. View all weather logs
3. View statistics
4. Clear all logs
5. Exit

Enter your choice: 5
```
