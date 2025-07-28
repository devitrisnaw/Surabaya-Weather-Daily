# data_cleaning.py

import pandas as pd

def clean_weather_data(df):
    # Pastikan kolom ada
    required_columns = ['time', 'temperature_2m_max', 'temperature_2m_min', 'precipitation_sum']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Kolom '{col}' tidak ditemukan dalam DataFrame.")
    
    # Ubah kolom 'time' ke format datetime
    df['date'] = pd.to_datetime(df['time'])

    # Drop baris yang belum memiliki data suhu (null)
    df = df.dropna(subset=['temperature_2m_min', 'temperature_2m_max'])

    # Tambahkan kolom suhu rata-rata
    df['avg_temperature'] = ((df['temperature_2m_max'] + df['temperature_2m_min']) / 2).round(1)

    # Tambahkan kolom selisih suhu
    df['temperature_gap'] = (df['temperature_2m_max'] - df['temperature_2m_min']).round(1)

    # Tambahkan kolom boolean apakah hari tersebut hujan
    df['has_rain'] = df['precipitation_sum'] > 0

    # Susun ulang kolom biar rapi
    df_cleaned = df[['date', 'temperature_2m_min', 'temperature_2m_max', 'avg_temperature', 'temperature_gap', 'precipitation_sum', 'has_rain']]

    return df_cleaned


# Uji coba lokal
if __name__ == "__main__":
    # Load dari file hasil ekstraksi sebelumnya (Windows fix)
    df_raw = pd.read_csv(r"C:\Users\hp\Downloads\Purwadhika\Modul 2\porto_weather\data\surabaya_weather_last30days.csv")
    df_clean = clean_weather_data(df_raw)
    df_clean.to_csv("surabaya_weather_clean.csv", index=False)
    print("✅ Data hasil transformasi disimpan ke surabaya_weather_clean.csv")
