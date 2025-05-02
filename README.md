# PTT Alertor

一個簡單可在本地建立的通知工具，並根據設定的條件查詢 PTT 看板（如關鍵字、推文數、作者）透過 **Discord Webhook** 發送通知。

[![Docker Downloads][Docker-Image]][Docker-Url]

[Docker-Image]: https://img.shields.io/docker/pulls/willyaako/ptt-alertor
[Docker-Url]: https://hub.docker.com/r/willyaako/ptt-alertor

---

## 功能
- 支援多看板監控。
- 根據關鍵字、推文數或指定作者觸發通知 (case-insensitive)。
- 支援從 Google Drive 配置檔案讀取設定。
- 使用 **Discord Webhook** 發送即時通知。
- 可自定義監控間隔時間。

---

## 環境需求
- Python 3
- Docker
- **Discord Webhook URL**（請至 Discord 設定 Webhook: https://support.discord.com/hc/zh-tw/articles/228383668 ）

---

## Run with Docker

### 1. Pull Docker image

```sh
docker pull willyaako/ptt-alertor:latest
```

### 2. Configuration

需提供如下格式的 json 檔案，並上傳到 Github Private Repo。

範例：

```json
{
    "MacShop": {
        "key": [["Homepod", "2"], ["iPhone", "16"]],
        "push": 50,
        "author": ["aaa", "bbb"]
    }
}
```

#### 說明
- `key`: 關鍵字列表，符合所有條件才觸發通知。
- `push`: 推文數門檻，超過指定數量觸發通知。
- `author`: 指定作者發文時觸發通知。

### 3. Run container

#### 使用環境變數配置：

```sh
docker run -d \
    --name ptt-alert \
    -e GITHUB_TOKEN=1A2B3C4D5E6F \
    -e GITHUB_FILE_URL=https://raw.githubusercontent.com/willyaako/ptt_alert_keyword/main/config.json
    -e FETCH_PERIOD=60 \
    -e DISCORD_WEBHOOK_URL=YOUR_DISCORD_WEBHOOK_URL \
    willyaako/ptt-alertor:latest
```

#### 說明
- `GITHUB_TOKEN`: 你的 GitHub Personal Access Token，用來授權存取私有 GitHub Repo。
- `GITHUB_FILE_URL`: 設定的 JSON 配置檔案 URL。
- `FETCH_PERIOD`: 設定多久檢查一次，單位是秒（如：60 表示每 60 秒檢查一次）
- `DISCORD_WEBHOOK_URL`: 你的 Discord Webhook URL，發送通知的目標。

---

## ToDo List
- 設定檔可直接讀取本機檔案

