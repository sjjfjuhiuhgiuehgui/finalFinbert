from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import os  
import re
import subprocess


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

# 執行finbert
print("執行finbert")
script_path = r"C:\Users\teter\Desktop\KaiPython\金十\finalfinbert.py"
subprocess.run(["python", script_path])


# 執行下一個timer
print("執行timer")
script_path = r"C:\Users\teter\Desktop\KaiPython\金十\timer.py"
subprocess.run(["python", script_path])

# 執行下一個loop
print("執行loop")
script_path = r"C:\Users\teter\Desktop\KaiPython\金十\loop.py"
subprocess.run(["python", script_path])
