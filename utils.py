def print_divider():
    print("=" * 50)

def display_weather(record):
    print_divider()
    print(f"City         : {record['city']}")
    print(f"Temperature  : {record['temperature']} °C")
    print(f"Humidity     : {record['humidity']} %")
    print(f"Pressure     : {record['pressure']} hPa")
    print(f"Wind Speed   : {record['wind_speed']} m/s")
    print(f"Condition    : {record['condition']}")
    print(f"Timestamp    : {record['timestamp']}")
    print_divider()
