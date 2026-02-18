from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Put your Discord webhook URL here
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1473719134721278089/iIDmXfy7wue_NnwCgq6OmwTkdt_tro3rS58jbpW_QdYeV9m_dhr6syMRQcMqwdaxnsJw"

@app.route("/clickup-webhook", methods=["POST"])
def clickup_webhook():
    data = request.json

    # Extract useful info (adjust fields as needed)
    task_name = data.get("task", {}).get("name", "No name")
    task_status = data.get("task", {}).get("status", {}).get("status", "Unknown")
    task_url = data.get("task", {}).get("url", "")

    # Format a simple Discord message
    discord_data = {
        "content": f"Task Updated: {task_name}\nStatus: {task_status}\nLink: {task_url}"
    }

    # Send to Discord
    response = requests.post(DISCORD_WEBHOOK_URL, json=discord_data)
    if response.status_code != 204:
        print("Discord error:", response.text)

    return jsonify({"ok": True})

if __name__ == "__main__":
    # Listen on all interfaces, port 5000
    app.run(host="0.0.0.0", port=5000)