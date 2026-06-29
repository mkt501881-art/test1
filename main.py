from flask import Flask, request
import requests
import os

app = Flask(__name__)

WEBHOOK = "https://discord.com/api/webhooks/1521071657349812314/NYpXoNoz_4rrQN35Px5pUPAjGRhb9ZyKdgc-z_QqA3GbaSYMObUeNd1sTFHPzJLTCtJy"
TOKEN = "doingtest"

@app.route("/update", methods=["POST"])
def update():
    data = request.json

    print("received:", data)

    if data.get("token") != TOKEN:
        return "unauthorized", 403

    memory = data.get("memory")

    msg = f"テスト {memory}"

    try:
        res = requests.post(WEBHOOK, json={"content": msg})
        print("status:", res.status_code)
        print("response:", res.text)
    except Exception as e:
        print("error:", e)

    return "ok"

port = int(os.environ.get("PORT", 5000))

app.run(host="0.0.0.0", port=port)
