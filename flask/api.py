import env
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
PORT = 3000


@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.json
        print(data)  # print all response

        message_from = data["data"]["from"]  # sender number
        message_msg = data["data"]["body"]  # Message text
        print(data)

        # Assuming you want to call the replyMessage function here
        reply_message(data)

        return jsonify(success=True), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify(success=False, error=str(e)), 500


@app.route("/")
def home():
    print("hola loko")
    # Assuming you want to call the replyMessage function here
    reply_message(request.json)
    return jsonify(success=True), 200


def reply_message(input_data):
    url = "https://graph.facebook.com/v17.0/222849127571783/messages"
    access_token = "EAAX21TVIX8gBO1LGIKDKCV2hGU1LGdDQuPdQ1FZAY666KBKKczSFMZCvlMvdGewVhK3mbZAGJ8Uk1mYOZBWxUeAfMAmAY5ic4bwI6rzdDLZAMp2RIHcZAb1Nh1qInrGgPIZAcfF0SZCZC7zZAgNNgO6jnZBSO6pOYxkkY35W9ZAbbhXVV1IC4xHb8HDFDpZAwigEaN379Ips2mKDw9xgvZBJM7XQRZAZAVWdqUgZD"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    data = {
        "messaging_product": "whatsapp",
        "to": "541154933738",
        "type": "template",
        "template": {"name": "hello_world", "language": {"code": "en_US"}},
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        print("Respuesta:", response.json())
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")


if __name__ == "__main__":
    app.run(port=PORT, debug=True)
