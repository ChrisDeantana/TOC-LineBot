from transitions.extensions import GraphMachine

from linebot.models import MessageTemplateAction
from utils import send_text_message, send_carousel_message, send_button_message, send_image_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_characters(self, event):
        text = event.message.text
        return text.lower() == 'choose'

    def on_enter_characters(self, event):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Choose Hiragana Or Katakana"))
        #send_text_message(event.reply_token, 'Choose Hiragana Or Katakana')

    def is_going_to_hiragana(self, event):
        text = event.message.text
        return text.lower() == 'hiragana'

    def on_enter_hiragana(self, event):
        send_text_message(event.reply_token, 'Display The Hiragana')

    def is_going_to_katakana(self, event):
        text = event.message.text
        return text.lower() == 'katakana'

    def on_enter_katakana(self, event):
        send_text_message(event.reply_token, 'Display The Katakana')

