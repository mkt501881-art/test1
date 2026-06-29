from flask import Flask, request
import requests
import os

app = Flask(__name__)

WEBHOOK = "https://discord.com/api/webhooks/1521071657349812314/NYpXoNoz_4rrQN35Px5pUPAjGRhb9ZyKdgc-z_QqA3GbaSYMObUeNd1sTFHPzJLTCtJy"
TOKEN = "doingtest"

@app.route("/update", methods=["POST"])
def update():
    print("=== request received ===")

    data = request.json
    print("data:", data)

    if not data:
        print("no data")
        return "bad request", 400

    if data.get("token") != TOKEN:
        print("token mismatch")
        return "unauthorized", 403

    memory = data.get("memory")
    print("memory:", memory)

    msg = f"テスト {memory}%"

    try:
        print("sending to discord...")
        res = requests.post(WEBHOOK, json={"content": msg})
        print("discord status:", res.status_code)
        print("discord response:", res.text)
    except Exception as e:
        print("discord error:", e)

    print("=== finished ===")
    return "ok"

port = int(os.environ.get("PORT", 5000))

app.run(host="0.0.0.0", port=port)
