import os
import requests
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def load_config(key):
    return os.getenv(key)

def load_line_token():
    token = os.getenv("LINE_TOKEN")
    if not token:
        raise ValueError("環境變數 LINE_TOKEN 未設置，請檢查！")
    return token

def update_keyword_dict(file_url):
    try:
        response = requests.get(file_url)
        response.raise_for_status()
        return json.loads(response.content.decode('utf-8'))
    except Exception as e:
        print("更新關鍵字字典失敗:", e)
        return {}
    
def load_config_from_json(file_path="config.json"):
    """
    從本地 JSON 檔案讀取設定。
    :param file_path: JSON 檔案的路徑
    :return: 配置的字典
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"配置檔案 {file_path} 不存在，請檢查！")
    
    with open(file_path, "r", encoding="utf-8") as file:
        config = json.load(file)
        return config