import requests
from utils.config import load_config

DISCORD_WEBHOOK_URL = load_config("DISCORD_WEBHOOK_URL")

def send_discord_message(message):
    if not DISCORD_WEBHOOK_URL:
        print("❌ Discord Webhook URL 未設定！")
        return

    payload = {"content": message}
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        if response.status_code == 204:
            print("✅ 訊息已成功發送到 Discord")
        else:
            print(f"❌ 發送失敗，狀態碼: {response.status_code}")
    except Exception as e:
        print("❌ 發送 Discord 訊息時發生錯誤:", e)
