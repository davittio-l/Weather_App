import requests
import pandas as pd
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = 'http://api.openweathermap.org/data2.5/onecall'

def get_weather_data(lat, lon):
    params = {
        'lat': lat,
        'lon': lon,
        'exclude': 'minutely,hourly',
        'appid': API_KEY,
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

def process_weather_data(data):
    daily_data = data['daily']
    weather_records = []

    for day in daily_data:
        date = datetime.datetime.fromtimestamp(day['dt']).strftime('%Y-%m-%d')
        temp = day['temp']['day']
        rainfall =day.get('rain', 0)
        weather_records.append([date, temp, rainfall])
    
    df = pd.DataFrame(weather_records, columns=['Date', 'Temperature', 'Rainfall'])
    return df

def main():
    lat, lon = 35.7565, -83.9705
    weather_data = get_weather_data(lat, lon)
    df = process_weather_data(weather_data)
    df.to_csv('weather_data.csv', index=False)
    print("Weather data saved to weather_data.csv")

if __name__ == '__main__':
    main()