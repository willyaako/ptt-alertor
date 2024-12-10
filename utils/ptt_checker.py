import requests
from bs4 import BeautifulSoup
from utils.line_notify import line_notify_message

def check_board(board, keyword_dict, token, sended):
    try:
        response = requests.get(f"https://www.ptt.cc/bbs/{board}/index.html")
        soup = BeautifulSoup(response.text, "html.parser")
        posts = soup.select("div.r-ent")
        for post in posts:
            title_element = post.select_one("div.title a")
            if not title_element:
                continue
            title = title_element.text
            url = f"https://www.ptt.cc{title_element['href']}"
            author = post.select_one("div.meta div.author").text
            push_num = post.select_one("div.nrec span")
            push_num = "100" if push_num and push_num.text == "爆" else (push_num.text if push_num else "0")

            for keytype, values in keyword_dict.get(board, {}).items():
                if keytype == "key":
                    # 檢查是否有匹配的 keys
                    matching_keys = next((keys for keys in values if all(word.lower() in title.lower() for word in keys)), None)
                    if matching_keys:
                        notify(board, "key", push_num, title, url, "&".join(matching_keys), token, sended)
                elif keytype == "push" and push_num.isdigit() and int(push_num) >= values:
                    notify(board, "push", push_num, title, url, push_num, token, sended)
                elif keytype == "author" and author in values:
                    notify(board, "author", push_num, title, url, author, token, sended)
    except Exception as e:
        print("檢查看板錯誤:", e)

def notify(board, keytype, push_num, title, url, msg, token, sended):
    if url not in sended:
        message = f"{msg}@{board}\n看板：{board} ; {keytype}：{msg}\n\n推文數：{push_num}\n {title}\n{url}"
        line_notify_message(token, message)
        sended.append(url)
        print(message)