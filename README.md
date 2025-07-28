# 🌤️ Surabaya Weather ETL (Daily)

Hey there! This is a simple end-to-end ETL project that pulls daily weather data for **Surabaya, Indonesia** using the Open-Meteo public API. The data gets cleaned, transformed, sent to Google BigQuery, and then visualized using Looker Studio.

---

## 🎯 What This Project Does

- Pulls daily weather data from Open-Meteo
- Cleans and transforms the raw data
- Calculates helpful features like average temperature, temperature gap, and rain indicator
- Loads everything into BigQuery for further analysis
- Displays the data using a live dashboard on Looker Studio

---

## 🔧 Tech Stack

- **Python 3.10+**
- **Libraries:** pandas, requests, google-cloud-bigquery
- **Storage:** Google BigQuery
- **Visualization:** Looker Studio
---

## 🛠️ How to Run This Project (Manual ETL)

1. **Install all dependencies**
   ```bash
   pip install -r requirements.txt
   
---

## 🧱 ETL project flow

```text
Open-Meteo API
     ↓
extract.py
     ↓
transform.py
     ↓
load.py
     ↓
BigQuery Table (surabaya_weather)
     ↓
Looker Studio Dashboard
```

---

## 📊 Dashboard
You can view the weather trends and insights here:

👉 View Looker Studio Dashboard

https://lookerstudio.google.com/reporting/edbae31e-f3da-434d-afe6-9578a68d03c4
(The link is also saved in dashboard_link.txt)
