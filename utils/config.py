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
    print("🔹 GITHUB_FILE_URL:", load_config("GITHUB_FILE_URL"))

def update_keyword_dict(file_url):
    try:
        github_token = load_config("GITHUB_TOKEN")  # 從環境變數取得 GitHub token
        headers = {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github.v3.raw"
        }
        response = requests.get(file_url, headers=headers)
        response.raise_for_status()
        return json.loads(response.content.decode('utf-8'))
    except Exception as e:
        print("更新關鍵字字典失敗:", e)
        return {}