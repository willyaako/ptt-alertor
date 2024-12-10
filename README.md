# PTT Alert System
一個簡單可在本地建立的通知工具，並根據設定的條件查詢 PTT 看板（如關鍵字、推文數、作者）透過 LINE Notify 發送通知。

 [![Docker Downloads][Docker-Image]][Docker-Url]

[Docker-Image]: https://img.shields.io/docker/pulls/willyaako/ptt-alertor
[Docker-Url]: https://hub.docker.com/r/willyaako/ptt-alertor

***
# 功能
- 支援多看板監控。
- 根據關鍵字、推文數或指定作者觸發通知 (case-insensitive)。
- 支援從 Google Drive 配置檔案讀取設定。
- 使用 LINE Notify 發送即時通知。
- 可自定義監控間隔時間。
***
# 環境需求
- Python 3
- Docker
- LINE Notify Token
  ( 請至 Line 官網取得token: https://notify-bot.line.me/my/ )


***
# 安裝與使用

### 1. 安裝依賴套件

如果您想直接運行程式：

```sh
pip install -r requirements.txt
```
### 2. 配置文件
需提供如下格式的檔案 config.json, 並上傳到 GoogleDrive, 需公開檔案並記錄 File ID

example: 
https://drive.google.com/file/d/{GOOGLE_FILE_ID}/view?usp=drive_link

```json
{
    "MacShop": {
        "key": [["HomePod", "2"], ["iPhone", "16"]],
        "push": 50,
        "author": ["aaa", "bbb"]
    }
}
```
#### 說明
- key: 關鍵字列表，符合所有條件才觸發通知。
- push: 推文數門檻，超過指定數量觸發通知。
- author: 指定作者發文時觸發通知。
  
### 3. 設定環境變數

#### 建立 .env 檔案：

```makefile
GOOGLE_FILE_ID=YOUR_GOOGLE_FILE_ID
FETCH_PERIOD=60
LINE_NOTIFY_TOKEN=YOUR_LINE_TOKEN_HERE
```

### 4. 運行程式

```bash
python main.py
```


# 使用 Docker
### 1. Pull Docker image

```sh
docker pull willyaako/ptt-alertor:latest
```
### 2. 配置文件
需提供如下格式的檔案 config.json, 並上傳到 GoogleDrive, 需公開檔案並記錄 File ID

example: 
https://drive.google.com/file/d/{GOOGLE_FILE_ID}/view?usp=drive_link

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
  
### 3. 運行容器
#### 使用環境變數配置：

```sh
docker run -d \
    --name ptt-alert \
    -e GOOGLE_FILE_ID=1A2B3C4D5E6F \
    -e FETCH_PERIOD=60 \
    -e LINE_NOTIFY_TOKEN=YOUR_LINE_TOKEN_HERE \
    willyaako/ptt-alertor:latest
```

### ToDo List
- 設定檔可直接讀取本機檔案

