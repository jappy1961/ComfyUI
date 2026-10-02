#!/usr/bin/env python3
import sys
import json
import urllib.request

BOT_TOKEN = "8756944347:AAH3WWzHOJopBlpEBxJtcfdfmn9305Dipgs"
CHAT_ID = "8343724201"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"Error sending Telegram message: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        msg = " ".join(sys.argv[1:])
    else:
        msg = "🤖 *[Antigravity Dell Workstation]* - Reporte de Estado"
    send_telegram(msg)
