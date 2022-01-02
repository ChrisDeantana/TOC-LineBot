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
        title = 'Lets learn Japanese'
        text = 'Choose『Hiragana』還是『Katakana』'
        btn = [
            MessageTemplateAction(
                label='Hiragana',
                text='Hiragana'
            ),
            MessageTemplateAction(
                label='Katakana',
                text='Katakana'
            ),
        ]
        url = 'https://i0.wp.com/blog.lingodeer.com/wp-content/uploads/2020/06/%E5%B9%B3%E5%81%87%E7%89%87%E5%81%87%E5%90%8D.png'
        send_button_message(event.reply_token, title, text, btn, url)
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

    def is_going_to_hiragana_basic(self, event):
        text = event.message.text
        return text.lower() == 'hiragana_basic'

    def on_enter_hiragana_basic(self, event):
        send_text_message(event.reply_token, 'Display The hiragana_basic')

    def is_going_to_hiragana_dakuon(self, event):
        text = event.message.text
        return text.lower() == 'hiragana_dakuon'

    def on_enter_hiragana_dakuon(self, event):
        send_text_message(event.reply_token, 'Display The hiragana_dakuon')

    def is_going_to_hiragana_small(self, event):
        text = event.message.text
        return text.lower() == 'hiragana_small'

    def on_enter_hiragana_small(self, event):
        send_text_message(event.reply_token, 'Display The hiragana_small')

    def is_going_to_hiragana_longvowels(self, event):
        text = event.message.text
        return text.lower() == 'hiragana_longvowels'

    def on_enter_hiragana_longvowels(self, event):
        send_text_message(event.reply_token, 'Display The hiragana_longvowels')

    def is_going_to_katakana_basic(self, event):
        text = event.message.text
        return text.lower() == 'katakana_basic'

    def on_enter_katakana_basic(self, event):
        send_text_message(event.reply_token, 'Display The katakana_basic')

    def is_going_to_katakana_dakuon(self, event):
        text = event.message.text
        return text.lower() == 'katakana_dakuon'

    def on_enter_katakana_dakuon(self, event):
        send_text_message(event.reply_token, 'Display The Katakana_dakuon')

    def is_going_to_katakana_combo(self, event):
        text = event.message.text
        return text.lower() == 'katakana_combo'

    def on_enter_katakana_combo(self, event):
        send_text_message(event.reply_token, 'Display The katakana_combo')

    def is_going_to_katakana_small(self, event):
        text = event.message.text
        return text.lower() == 'katakana_small'

    def on_enter_katakana_small(self, event):
        send_text_message(event.reply_token, 'Display The katakana_small')

    def is_going_to_katakana_longvowels(self, event):
        text = event.message.text
        return text.lower() == 'katakana_longvowels'

    def on_enter_katakana_longvowels(self, event):
        send_text_message(event.reply_token, 'Display The katakana_longvowels')

