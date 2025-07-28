# load_to_bigquery.py

import os
import pandas as pd
from google.cloud import bigquery

def load_to_bq(df, table_id, credentials_path):
    # Pastikan file kredensial ada
    if not os.path.exists(credentials_path):
        raise FileNotFoundError(f"Kredensial GCP tidak ditemukan: {credentials_path}")

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
    client = bigquery.Client()

    # Konfigurasi upload
    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE",
        autodetect=True,
        source_format=bigquery.SourceFormat.CSV,
    )

    # Simpan ke file CSV sementara
    temp_file = "temp_cleaned_weather.csv"
    df.to_csv(temp_file, index=False)

    # Upload ke BigQuery
    with open(temp_file, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_id, job_config=job_config)

    job.result()

    table = client.get_table(table_id)
    print(f"✅ Sukses upload {table.num_rows} baris ke {table_id}")


if __name__ == "__main__":
    # Atur path dinamis berdasarkan lokasi script
    base_dir = os.path.dirname(os.path.abspath(__file__))         # /ETL
    project_root = os.path.dirname(base_dir)                      # /porto_weather

    # Path ke file CSV
    csv_file = os.path.join(project_root, "data\surabaya_weather_clean.csv")
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"❌ File CSV tidak ditemukan: {csv_file}")

    df_clean = pd.read_csv(csv_file)

    # Path ke file kredensial
    credentials_path = os.path.join(project_root, "config\weatherdaily-467007-514221e7d7fb.json")
    table_id = "weatherdaily-467007.weather_data.surabaya_weather"

    load_to_bq(df_clean, table_id, credentials_path)
