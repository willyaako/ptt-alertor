import os

SENT_LIST_FILE = "./sended_urls.txt"

def load_sent_list():
    if os.path.exists(SENT_LIST_FILE):
        with open(SENT_LIST_FILE, 'r') as file:
            return file.read().splitlines()
    return []

def save_sent_list(sended):
    with open(SENT_LIST_FILE, 'w') as file:
        file.write("\n".join(sended))