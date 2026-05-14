import requests
import time

BOT_TOKEN = "8737848238:AAGNE41e3qZuakLMu10DrgxEh69NqUoSNq4"
CHAT_ID = "5745714729"

def send_signal(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": text
    }

    requests.post(url, data=data)

while True:
    signal = "📈 BUY SIGNAL EUR/USD"
    send_signal(signal)
    print("Signal Sent")

    time.sleep(60)
