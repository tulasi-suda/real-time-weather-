from weather_client import WeatherClient, WeatherAPIError
from db_manager import DatabaseManager
from utils import display_weather, print_divider

class WeatherApp:
    def __init__(self):
        self.client = WeatherClient()
        self.db = DatabaseManager()

    def menu(self):
        print("""
------------ Weather Application ---------------
1. Get weather for a city
2. View all weather logs
3. View statistics
4. Clear all logs
5. Exit
""")

    def run(self):
        while True:
            self.menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                city = input("Enter city name: ")

                try:
                    weather = self.client.get_weather(city)
                    display_weather(weather)
                    self.db.insert_log(weather)

                except WeatherAPIError as e:
                    print(f"Error: {e}")

            elif choice == "2":
                logs = self.db.fetch_logs()
                print_divider()
                for log in logs:
                    print(log)
                print_divider()

            elif choice == "3":
                stats = self.db.get_statistics()
                print_divider()
                print("Average Temperature:", stats[0])
                print("Average Humidity   :", stats[1])
                print("Average Pressure   :", stats[2])
                print_divider()

            elif choice == "4":
                self.db.clear_logs()
                print("All logs cleared successfully.")

            elif choice == "5":
                print("Exiting program")
                break

            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    app = WeatherApp()
    app.run()
