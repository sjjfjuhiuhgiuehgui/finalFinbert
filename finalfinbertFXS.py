from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from bs4 import BeautifulSoup
import time
import csv
from googletrans import Translator
import pandas as pd
import requests






# 開啟瀏覽器視窗(Chrome)
driver = webdriver.Chrome()
url = "https://www.fxstreet.hk/news?q=&hPP=13&idx=FxsIndexPro&p=0&dFR%5BTags%5D%5B0%5D=%E6%AD%90%E5%85%83%2F%E7%BE%8E%E5%85%83"    
driver.get(url)  
time.sleep(3) 
tittle_list = []




tittle_elements = driver.find_elements(By.CLASS_NAME, 'fxs_headline_tiny')






for tittle_element in tittle_elements:
    tittle_list.append(tittle_element.text)


finalArray = [f"{tittle_list[i]}" for i in range(len(tittle_list))]





# 關閉瀏覽器
driver.quit()

# 指定输出文件名
csv_file = "C:\\Users\\teter\\Desktop\\KaiPython\\金十\\fxs.csv"

# 使用 csv 模块打开文件并写入数组数据
with open(csv_file, 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(["事件"])  # 写入 CSV 文件的标题行
    for item in finalArray:
        parts = item.split(",")
        writer.writerow(parts)

print("CSV 文件已成功生成：", csv_file)


#翻譯
# 初始化翻譯器
translator = Translator()

# 讀取CSV檔案
file_path = 'C:/Users/teter/Desktop/KaiPython/金十/fxs.csv'  # 確保路徑是正確的
data = pd.read_csv(file_path)

# 翻譯並將結果存儲在新列表中
translated_texts = []
for text in data['事件']:
    translated = translator.translate(text, src='zh-tw', dest='en').text  # 調整為適合您文本的語言代碼
    translated_texts.append(translated)

# 將所有翻譯後的文本合併成一個字符串，用逗號隔開
translated_text_combined = ', '.join(translated_texts)

# 創建一個新的DataFrame，其中只包含一個列，這個列將存儲合併後的翻譯文本
final_data = pd.DataFrame({'翻譯後事件': [translated_text_combined]})

# 將這個新DataFrame保存到CSV檔案中
output_file_path = 'C:/Users/teter/Desktop/KaiPython/金十/translated_output_only_D2.csv'
final_data.to_csv(output_file_path, index=False)

print(f'只包含翻譯後文本的檔案已保存到：{output_file_path}')


#分析
API_URL = "https://api-inference.huggingface.co/models/ProsusAI/finbert"
API_TOKEN = "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"

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

csv_file = "C:\\Users\\teter\\Desktop\\KaiPython\\金十\\translated_output_only_D2.csv"


# 初始化一個變量來存儲A2格的內容
a2_content = None
with open(csv_file, 'r', encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # 跳過標題行
    for i, row in enumerate(csv_reader):
        if i == 0:
            a2_content = row[0]
            break

# 初始化重試次數和重試間隔（秒）
max_retries = 3
retry_interval = 10  # 重試間隔設為10秒

# 如果成功獲取了A2格的內容，則進行分析
if a2_content:
    for attempt in range(max_retries):
        output = query({"inputs": a2_content})
        if 'error' in output:
            print(f"Error: {output['error']}. Retrying in {retry_interval} seconds...")
            time.sleep(retry_interval)  # 等待一段時間後重試
        else:
            print(f"A2 Content: {a2_content}\nSentiment: {output}\n")
            break  # 如果成功獲得回應，則退出循環
    else:
        print("Max retries reached. Unable to get sentiment analysis.")
else:
    print("A2格的內容未找到。")