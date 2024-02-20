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




