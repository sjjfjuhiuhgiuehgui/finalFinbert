from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import os  
import re
import subprocess

# 开启浏览器窗口(Chrome)
driver = webdriver.Chrome()
url = "https://rili.jin10.com/"
driver.get(url)
time.sleep(5)  # 增加等待时间，以确保页面完全加载

# 指定输出文件名
csv_file = "C:\\Users\\teter\\Desktop\\KaiPython\\金十\\loop.csv"

# 如果文件已存在，先删除它
if os.path.exists(csv_file):
    os.remove(csv_file)

# 找到时间元素并直接写入CSV文件
with open(csv_file, 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(["时间"])  # 写入CSV文件的标题行
    time_elements = driver.find_elements(By.CLASS_NAME, 'timer')
    for time_element in time_elements:
        writer.writerow([time_element.text])  # 直接写入每个元素的文本

driver.quit()  # 关闭浏览器
print("CSV文件已成功生成：", csv_file)


csv_file = "loop.csv"
with open(csv_file, newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # 跳过标题行
    row = next(reader)  # 读取第一行数据
    time_text = row[0]  # 假设时间数据在第二列

# 解析时间文本
match = re.search(r"(\d+)小时(\d+)分后", time_text)
if match:
    hours = int(match.group(1))
    minutes = int(match.group(2))
    wait_seconds = (hours * 60 + minutes) * 60  # 转换为秒
else:
    wait_seconds = 0
    print("时间格式不匹配")

print(f"等待{wait_seconds}秒...")

# 等待指定的时间
time.sleep(wait_seconds)

# 执行另一个程序或脚本
print("執行loop")
# 替换为您的实际文件路径
script_path = r"C:\Users\teter\Desktop\KaiPython\金十\finalfinbert.py"
subprocess.run(["python", script_path])

