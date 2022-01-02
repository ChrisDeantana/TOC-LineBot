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
        "katakana_longvowels"
    ],
    transitions=[
        {'trigger': 'advance', 'source': 'user', 'dest': 'characters', 'conditions': 'is_going_to_characters'},
        {'trigger': 'advance', 'source': 'characters', 'dest': 'hiragana', 'conditions': 'is_going_to_hiragana'},
        {'trigger': 'advance', 'source': 'characters', 'dest': 'katakana', 'conditions': 'is_going_to_katakana'},
        {'trigger': 'advance', 'source': 'user', 'dest': 'characters', 'conditions': 'is_going_to_characters'},
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
channel_secret = os.getenv("LINE_CHANNEL_SECRET", "5a5d657db43746292fec10f360b32471")
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", "MBds+RkN+DOYmq1gldT0dlwDkGQVdi7bLfjpjx9FRGjqEIK57PSEFjY4EVraVPra5rwZYqRYfu5SUpB++SfgMTI9whg0+zWuv/u6No7JDm1m3OF/7usv9VgC3yAKOKEhzn6UgwwMl+/Lj00znsRlygdB04t89/1O/w1cDnyilFU=")
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

    # if event is MessageEvent and message is TextMessage, then echo text
    # for event in events:
    #     if not isinstance(event, MessageEvent):
    #         continue
    #     if not isinstance(event.message, TextMessage):
    #         continue
    #
    #     line_bot_api.reply_message(
    #         #event.reply_token, TextSendMessage(text=event.message.text)
    #         event.reply_token, TextSendMessage(text="Test!")
    #     )
    #     if event.message.text.lower() == "happy birthday":
    #         send_text_message(event.reply_token, "thank you")

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
            if event.message.text.lower() == 'fsm':
                send_image_message(event.reply_token, 'https://f74062044.herokuapp.com/show-fsm')
            elif machine.state != 'user' and event.message.text.lower() == 'restart':
                send_text_message(event.reply_token,
                                  '輸入『fitness』即可開始使用健身小幫手。\n隨時輸入『chat』可以跟機器人聊天。\n隨時輸入『restart』可以從頭開始。\n隨時輸入『fsm』可以得到當下的狀態圖。')
                machine.go_back()
            elif machine.state == 'user':
                send_text_message(event.reply_token,
                                  '輸入『fitness』即可開始使用健身小幫手。\n隨時輸入『chat』可以跟機器人聊天。\n隨時輸入『restart』可以從頭開始。\n隨時輸入『fsm』可以得到當下的狀態圖。')

            elif machine.state == 'hiragana':
                send_text_message(event.reply_token, '請輸入『男生』或『女生』')
            elif machine.state == 'katakana':
                send_text_message(event.reply_token, '請輸入一個『0~7的整數』')
            elif machine.state == 'hiragana_basic':
                send_text_message(event.reply_token, '請輸入『增肌』或『減脂』')
            elif machine.state == 'katakana_basic':
                send_text_message(event.reply_token, '輸入『熱量』可以查看您一天所需的熱量。\n輸入『影片』可以觀看健身影片。\n輸入『back』可重新選擇目標。')
            # elif machine.state == 'show_cal':
            #     if event.message.text.lower() == 'bmr':
            #         text = '即基礎代謝率，全名為 Basal Metabolic Rate。基礎代謝意思是身體為了要維持運作，在休息時消耗掉的熱量。基礎代謝率佔了總熱量消耗的一大部分。會影響到基礎代謝率高低的有很多，像是總體重、肌肉量、賀爾蒙、年齡等。'
            #         send_text_message(event.reply_token, text)
            #     elif event.message.text.lower() == 'tdee':
            #         text = '即每日總消耗熱量，全名為 Total Daily Energy Expenditure。指的是人體在一天內消耗的熱量，除了基礎代謝率所需的能量以外，還包括運動和其他活動消耗的熱量，像是走路、上下樓梯、活動肌肉等等。通常運動量愈大，TDEE也會愈高。'
            #         send_text_message(event.reply_token, text)
            #     elif event.message.text.lower() != 'back':
            #         send_text_message(event.reply_token, '輸入『食物』可以查看一天的熱量應如何攝取。\n輸入『BMR』或『TDEE』會有文字說明。\n輸入『back』返回選單。')

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
