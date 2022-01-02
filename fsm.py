from transitions.extensions import GraphMachine

from linebot.models import MessageTemplateAction
from utils import send_text_message, send_carousel_message, send_button_message, send_image_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_characters(self, event):
        text = event.message.text
        return text.lower() == "choose"

    def on_enter_characters(self, event):
        # title = 'Choose what you want to learn'
        # text = 'Choose『Hiragana』Or『Katakana』'
        # btn = [
        #     MessageTemplateAction(
        #         label='Hiragana',
        #         text='Hiragana'
        #     ),
        #     MessageTemplateAction(
        #         label='Katakana',
        #         text='Katakana'
        #     ),
        # ]
        # url = 'https://i0.wp.com/blog.lingodeer.com/wp-content/uploads/2020/06/%E5%B9%B3%E5%81%87%E7%89%87%E5%81%87%E5%90%8D.png'
        # send_button_message(event.reply_token, title, text, btn, url)
        send_text_message(event.reply_token, 'Choose『Hiragana』Or『Katakana』')

    def is_going_to_hiragana(self, event):
        global charHorK
        text = event.message.text

        if text == 'Hiragana':
            charHorK = 'Hiragana'
            return True
        elif text == 'Katakana':
            charHorK = 'Katakana'
            return True
        return False

    def on_enter_hiragana(self, event):
        send_text_message(event.reply_token, 'Display The Hiragana')

    def is_going_to_katakana(self, event):
        global charHorK
        text = event.message.text

        if text == 'Hiragana':
            charHorK = 'Hiragana'
            return True
        elif text == 'Katakana':
            charHorK = 'Katakana'
            return True
        return False

    def on_enter_katakana(self, event):
        send_text_message(event.reply_token, 'Display The Katakana')

