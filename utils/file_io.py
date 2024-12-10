import os

def load_sent_list(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    return []

def save_sent_list(file_path, sended):
    with open(file_path, 'w') as file:
        file.write("\n".join(sended))
