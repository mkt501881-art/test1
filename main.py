from flask import Flask, request
import requests

app = Flask(__name__)

WEBHOOK = "https://discord.com/api/webhooks/1521071657349812314/NYpXoNoz_4rrQN35Px5pUPAjGRhb9ZyKdgc-z_QqA3GbaSYMObUeNd1sTFHPzJLTCtJy"
TOKEN = "doingtest"

@app.route("/update", methods=["POST"])
def update():
    data = request.json

    if data.get("token") != TOKEN:
        return "unauthorized", 403

    memory = data.get("memory")

    msg = f"💻 メモリ使用率: {memory}%"

    requests.post(WEBHOOK, json={"content": msg})

    return "ok"

app.run()
