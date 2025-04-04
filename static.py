import requests
from bs4 import BeautifulSoup
import json

# 設定 CNYES 台積電 (2330) 股價資訊頁面 URL
url = 'https://www.cnyes.com/twstock/2330'

# 設定請求標頭，模擬瀏覽器發送請求，避免被網站封鎖
headers = {"User-Agent": "Mozilla/5.0"}

# 發送 HTTP GET 請求
response = requests.get(url, headers=headers)

# 使用 BeautifulSoup 解析 HTML 內容
soup = BeautifulSoup(response.text, "html.parser")

# 初始化字典來存儲股價資訊，避免重複數據
stock_data = {}

# 只選取 `<li>` 裡的標籤
for item in soup.select("li.jsx-4238438383"):
    label_element = item.find('span', class_='jsx-4238438383 label')  # 標籤名稱
    value_element = item.find('span', class_='jsx-4238438383 value')  # 對應數值
    
    # 確保標籤與數值存在，避免程式發生錯誤
    if label_element and value_element:
        label = label_element.get_text(strip=True)  # 取得標籤文字
        value = value_element.get_text(strip=True)  # 取得數值文字
        
        # 避免重複數據
        if label not in stock_data:
            stock_data[label] = value

# 將擷取的股價資訊儲存為 JSON 檔案
with open("static.json", "w", encoding="utf-8") as f:
    json.dump(stock_data, f, ensure_ascii=False, indent=4)

# 印出擷取到的股價資訊，方便查看結果
print(json.dumps(stock_data, indent=4, ensure_ascii=False))
