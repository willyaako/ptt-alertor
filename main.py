import time
import traceback
import json
from datetime import datetime
from utils.config import load_config, update_keyword_dict
from utils.ptt_checker import check_board
from utils.file_io import load_sent_list, save_sent_list
from utils.discord_notify import send_discord_message

if __name__ == "__main__":
    print(datetime.now(), "📢 PTT ALERT START")

    FIRSTBOOT_CHECK_FLAG = True
    config_file_url = load_config("GITHUB_FILE_URL")
    wait_time = int(load_config("FETCH_PERIOD"))

    sended = load_sent_list()
    last_keyword_dict = None  # 用來記錄上次的關鍵字
    send_discord_message(f"📢 {datetime.now()} PTT ALERT START")
    while True:
        try:
            keyword_dict = update_keyword_dict(config_file_url, last_keyword_dict)
            # 這裡應該加入從 Google Drive 讀取 JSON 設定的邏輯
            # 檢查關鍵字是否有變更
            if last_keyword_dict is None or json.dumps(keyword_dict, sort_keys=True) != json.dumps(last_keyword_dict, sort_keys=True):
                print("\n🎯 監聽條件變更！當前監聽的看板與條件：")
                discord_message = "**🔍 監聽條件更新！當前監聽的看板與關鍵字**\n"

                for board, conditions in keyword_dict.items():
                    print(f"📌  看板：{board}")
                    discord_message += f"📌 **{board}**\n"

                    for keytype, values in conditions.items():
                        print(f"   🔍 {keytype}：{values}")
                        discord_message += f"   🔍 {keytype}: {values}\n"

                print("-" * 40)  # 分隔線

                send_discord_message(discord_message)
                # 更新 last_keyword_dict
                last_keyword_dict = keyword_dict

            for board in keyword_dict:
                check_board(board, keyword_dict, sended)

            FIRSTBOOT_CHECK_FLAG = False
            time.sleep(wait_time)
        except KeyboardInterrupt:
            save_sent_list(sended)
            send_discord_message(f"🛑 {datetime.now()} PTT ALERT STOP")
            break
        except Exception as e:
            errorMsg = datetime.now(), "❌ Error:", e
            print(errorMsg)
            send_discord_message(errorMsg)
            traceback.print_exc()
            time.sleep(10)
