import requests, time, os
TOKEN = os.environ.get("TOKEN")
def main():
    last_id = 0
    while True:
        try:
            url = f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset={last_id+1}&timeout=30"
            r = requests.get(url, timeout=35).json()
            for u in r.get('result', []):
                last_id = u['update_id']
                chat_id = u['message']['chat']['id']
                txt = u['message'].get('text','')
                if "/start" in txt:
                    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": chat_id, "text": "سلام! ربات 24 ساعته روشن شد ✅"})
        except:
            time.sleep(5)
if __name__ == "__main__":
    main()
