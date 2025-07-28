# data_extraction_harian.py

import requests
import pandas as pd
from datetime import datetime, timedelta

def fetch_weather_data(start_date, end_date):
    # Koordinat Surabaya
    latitude = -7.2575
    longitude = 112.7521

    # API Endpoint
    url = "https://archive-api.open-meteo.com/v1/archive"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "Asia/Bangkok"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    df = pd.DataFrame(data['daily'])
    return df

if __name__ == "__main__":
    # Ambil data dari 30 hari terakhir
    today = datetime.today().date()
    start_date = (today - timedelta(days=30)).isoformat()
    end_date = today.isoformat()

    print(f"Fetching weather data for Surabaya from {start_date} to {end_date}...")
    df_weather = fetch_weather_data(start_date, end_date)

    # Simpan ke file CSV
    filename = f"surabaya_weather_last30days.csv"
    df_weather.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
