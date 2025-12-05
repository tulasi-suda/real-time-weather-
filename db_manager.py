import sqlite3
from config import Config

class DatabaseManager:
    def __init__(self, db_name=Config.DB_NAME):
        self.db_name = db_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS city_weather_reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT,
                temperature REAL,
                humidity REAL,
                pressure REAL,
                wind_speed REAL,
                condition TEXT,
                timestamp TEXT
            )
        """)
        conn.commit()
        conn.close()

    def insert_log(self, record):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO city_weather_reports 
            (city, temperature, humidity, pressure, wind_speed, condition, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            record["city"], record["temperature"], record["humidity"],
            record["pressure"], record["wind_speed"], record["condition"], record["timestamp"]
        ))
        conn.commit()
        conn.close()

    def fetch_logs(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM city_weather_reports")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def clear_logs(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM city_weather_reports")
        conn.commit()
        conn.close()

    def get_statistics(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                AVG(temperature),
                AVG(humidity),
                AVG(pressure)
            FROM city_weather_reports
        """)
        stats = cursor.fetchone()
        conn.close()
        return stats
