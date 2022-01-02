import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=[
        "user",
        "characters",
        "hiragana",
        "katakana",
        "hiragana_basic",
        "hiragana_dakuon",
        "hiragana_combo",
        "hiragana_small",
        "hiragana_longvowels",
        "katakana_basic",
        "katakana_dakuon",
        "katakana_combo",
        "katakana_small",
        "katakana_longvowels",
        "restart"
    ],
    transitions=[
        {'trigger': 'advance', 'source': 'user', 'dest': 'characters', 'conditions': 'is_going_to_characters'},
        {'trigger': 'advance', 'source': 'characters', 'dest': 'hiragana', 'conditions': 'is_going_to_hiragana'},
        {'trigger': 'advance', 'source': 'characters', 'dest': 'katakana', 'conditions': 'is_going_to_katakana'},
        {'trigger': 'advance', 'source': 'hiragana', 'dest': 'hiragana_basic', 'conditions': 'is_going_to_hiragana_basic'},
        {'trigger': 'advance', 'source': 'hiragana', 'dest': 'hiragana_dakuon', 'conditions': 'is_going_to_hiragana_dakuon'},
        {'trigger': 'advance', 'source': 'hiragana', 'dest': 'hiragana_combo', 'conditions': 'is_going_to_hiragana_combo'},
        {'trigger': 'advance', 'source': 'hiragana', 'dest': 'hiragana_small', 'conditions': 'is_going_to_hiragana_small'},
        {'trigger': 'advance', 'source': 'hiragana', 'dest': 'katakana_longvowels', 'conditions': 'is_going_to_hiragana_longvowels'},
        {'trigger': 'advance', 'source': 'katakana', 'dest': 'katakana_basic', 'conditions': 'is_going_to_katakana_basic'},
        {'trigger': 'advance', 'source': 'katakana', 'dest': 'katakana_dakuon', 'conditions': 'is_going_to_katakana_dakuon'},
        {'trigger': 'advance', 'source': 'katakana', 'dest': 'katakana_combo', 'conditions': 'is_going_to_katakana_combo'},
        {'trigger': 'advance', 'source': 'katakana', 'dest': 'katakana_small', 'conditions': 'is_going_to_katakana_small'},
        {'trigger': 'advance', 'source': 'katakana', 'dest': 'katakana_longvowels', 'conditions': 'is_going_to_katakana_longvowels'},
        {
            "trigger": "go_back",
            "source": [
                "user",
                "characters",
                "hiragana",
                "katakana",
                "hiragana_basic",
                "hiragana_dakuon",
                "hiragana_combo",
                "hiragana_small",
                "hiragana_longvowels",
                "katakana_basic",
                "katakana_dakuon",
                "katakana_combo",
                "katakana_small",
                "katakana_longvowels"
            ],
            "dest": "user"
        },
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")

        response = machine.advance(event)

        if response == False:
            #send_text_message(event.reply_token, "Please choose one of the following!")
            #if machine.state == 'user':
            send_text_message(event.reply_token, "Please choose one of the following!")
            title = 'Lets learn Japanese'
            text = 'Choose『Characters』Or『Vocabulary』Or『FSM』'
            btn = [
                MessageTemplateAction(
                    label='Characters',
                    text='Characters'
                ),
                MessageTemplateAction(
                    label='Vocabulary',
                    text='Vocabulary'
                ),
                MessageTemplateAction(
                    label='FSM',
                    text='FSM'
                ),
            ]
            url = 'https://assets.website-files.com/5cdc34afa4217f8020168210/5e06163d20470442a540712b_languageIcon_japanese.png'
            send_button_message(event.reply_token, title, text, btn, url)

    return "OK"

@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
