from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import os
import re
import subprocess

while True:  # 創建一個無限循環
    # 執行finbert
    print("執行finbert")
    script_path_finbert = r"C:\Users\teter\Desktop\KaiPython\金十\finalfinbertFXS.py"
    subprocess.run(["python", script_path_finbert])

    

    print("等待五分鐘...")
    time.sleep(300)  # 等待300秒，即五分鐘