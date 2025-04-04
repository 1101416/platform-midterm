import requests
import csv

# 台灣證交所 API（台積電2330）
API_URL = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20250301&stockNo=2330"

response = requests.get(API_URL)
data = response.json()

# 提取有用的數據
stock_records = data.get("data", [])

# 儲存 CSV
with open("api.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["日期", "成交股數", "成交金額", "開盤價", "最高價", "最低價", "收盤價", "成交筆數"])
    writer.writerows(stock_records)

print("股票數據已儲存到 api.csv")
