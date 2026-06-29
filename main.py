from flask import Flask, request
import requests
import os

app = Flask(__name__)

WEBHOOK = "https://discord.com/api/webhooks/1521071657349812314/NYpXoNoz_4rrQN35Px5pUPAjGRhb9ZyKdgc-z_QqA3GbaSYMObUeNd1sTFHPzJLTCtJy"
TOKEN = "doingtest"

@app.route("/update", methods=["POST"])
def update():
    data = request.json

    if not data:
        return "bad request", 400

    if data.get("token") != TOKEN:
        return "unauthorized", 403

    memory = data.get("memory")

    if memory is None:
        return "no memory", 400

    msg = f"💻 メモリ使用率: {memory}%"

try:
    res = requests.post(WEBHOOK, json={"content": msg})
    print("status:", res.status_code)
    print("response:", res.text)
except Exception as e:
    print("error:", e)

    return "ok"

port = int(os.environ.get("PORT", 5000))

app.run(host="0.0.0.0", port=port)
