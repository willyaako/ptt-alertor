# PTT Alert System
PTT Alert System 是一個自動化的通知工具，用於監控 PTT 看板文章，並根據設定的條件（如關鍵字、推文數、作者）透過 LINE Notify 發送通知。
***
# 功能
- 支援多看板監控。
- 根據關鍵字、推文數或指定作者觸發通知。
- 支援從 Google Drive 配置檔案讀取設定。
- 使用 LINE Notify 發送即時通知。
- 可自定義監控間隔時間。
***
# 環境需求
- Python 3
- Docker（可選）
- LINE Notify Token
***
# 安裝與使用

### 1. 安裝依賴套件

如果您想直接運行程式：

```sh
pip install -r requirements.txt
```

### 2. 設定環境變數

#### 建立 .env 檔案：

```makefile
GOOGLE_FILE_ID=1A2B3C4D5E6F
FETCH_PERIOD=60
LINE_NOTIFY_TOKEN=YOUR_LINE_TOKEN_HERE
```

### 3. 運行程式

```bash
python main.py
```


# 使用 Docker
### 1. 建立 Docker 映像

```sh
docker build -t ptt-alert .
```

### 2. 運行容器
#### 使用環境變數配置：

```sh
docker run -d \
    --name ptt-alert \
    -e GOOGLE_FILE_ID=1A2B3C4D5E6F \
    -e FETCH_PERIOD=60 \
    -e LINE_NOTIFY_TOKEN=YOUR_LINE_TOKEN_HERE \
    ptt-alert
```


### 配置文件
需提供如下格式的檔案 config.json, 並上傳到 GoogleDrive：

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
- key: 關鍵字列表，符合所有條件才觸發通知。
- push: 推文數門檻，超過指定數量觸發通知。
- author: 指定作者發文時觸發通知。