import requests
import csv

#台灣證交所API（台積電2330）
API_URL = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20240301&stockNo=2330"

response = requests.get(API_URL)
data = response.json()

#從JSON物件data裡提取"data"這個欄位的資料
stock_records = data.get("data", [])

#在終端機顯示抓取到的數據
print("抓取的股票數據：")
for record in stock_records:
    print(record)
    
#儲存CSV
with open("api.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["日期", "成交股數", "成交金額", "開盤價", "最高價", "最低價", "收盤價", "成交筆數"])
    writer.writerows(stock_records)

print("股票數據已儲存到 api.csv")
