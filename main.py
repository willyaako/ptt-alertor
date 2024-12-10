import time
import traceback
from utils.line_notify import line_notify_message
from utils.config import load_config, update_keyword_dict
from utils.ptt_checker import check_board
from utils.file_io import load_sent_list, save_sent_list
from datetime import datetime

if __name__ == "__main__":
    token = ""
    FIRSTBOOT_CHECK_FLAG = True
    config_file_url = "https://drive.google.com/uc?id=" + load_config("GOOGLE_FILE_ID")
    wait_time = int(load_config("FETCH_PERIOD"))
    file_path = "./sended_urls.txt"

    keyword_dict = update_keyword_dict(config_file_url)
    sended = load_sent_list(file_path)

    token = load_config("LINE_TOKEN")
    if not token:
        print("無法取得 LINE Token")
        exit()
    print(datetime.now(), "PTT ALERT START")
    line_notify_message(token, f"{datetime.now()} PTT ALERT START")

    while True:
        try:
            keyword_dict = update_keyword_dict(config_file_url)
            for board in keyword_dict:
                if board != "line_token":
                    check_board(board, keyword_dict, token, sended)
            FIRSTBOOT_CHECK_FLAG = False
            time.sleep(wait_time)
        except KeyboardInterrupt:
            save_sent_list(file_path, sended)
            line_notify_message(token, f"{datetime.now()} PTT ALERT STOP")
            break
        except Exception as e:
            print(datetime.now(), "Error:", e)
            traceback.print_exc()
            time.sleep(10)