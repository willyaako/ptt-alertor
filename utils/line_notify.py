import requests
from datetime import datetime

def line_notify_message(token, msg):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {'message': msg}
    try:
        response = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload)
        return response.status_code
    except Exception as e:
        print(datetime.now(), "LINE Notify Error:", e)