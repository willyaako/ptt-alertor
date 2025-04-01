import json
import os
import requests
from dotenv import load_dotenv

# 載入 .env 檔案
load_dotenv()

def load_config(key):
    """ 從 .env 讀取設定 """
    return os.getenv(key)

# 測試讀取環境變數
if __name__ == "__main__":
    print("🔹 DISCORD_WEBHOOK_URL:", load_config("DISCORD_WEBHOOK_URL"))
    print("🔹 FETCH_PERIOD:", load_config("FETCH_PERIOD"))
    print("🔹 GOOGLE_FILE_ID:", load_config("GOOGLE_FILE_ID"))

def update_keyword_dict(file_url):
    try:
        response = requests.get(file_url)
        response.raise_for_status()
        return json.loads(response.content.decode('utf-8'))
    except Exception as e:
        print("更新關鍵字字典失敗:", e)
        return {}