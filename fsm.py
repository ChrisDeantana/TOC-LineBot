from transitions.extensions import GraphMachine

from linebot.models import MessageTemplateAction
from utils import send_text_message, send_button_message, send_image_message

#https://apieceofsushi.com/wp-content/uploads/2020/09/HiraganaChartPinkAPIECEOFSUSHI.COM_-500x707.png - hiragana
#https://apieceofsushi.com/wp-content/uploads/2020/09/KatakanaChartBlackAPIECEOFSUSHI.COM_.png - katakana

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_characters(self, event):
        text = event.message.text
        return text.lower() == 'characters'

    def on_enter_characters(self, event):
        title = 'Lets learn Japanese'
        text = 'Choose『Hiragana』Or『Katakana』'
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

    def is_going_to_hiragana(self, event):
        text = event.message.text
        return text.lower() == 'hiragana'

    def on_enter_hiragana(self, event):
        send_text_message(event.reply_token, 'Choose『Basic』Or『Dakuon』Or『Combo』Or『SmallnLongVowels』')

    def is_going_to_katakana(self, event):
        text = event.message.text
        return text.lower() == 'katakana'

    def on_enter_katakana(self, event):
        send_text_message(event.reply_token, 'Choose『Basic』Or『Dakuon』Or『Combo』Or『SmallnLongVowels』')

    def is_going_to_hiragana_basic(self, event):
        text = event.message.text
        return text.lower() == 'hiragana_basic'

    def on_enter_hiragana_basic(self, event):
        send_image_message(event.reply_token, 'https://apieceofsushi.com/wp-content/uploads/2020/09/HiraganaChartPinkAPIECEOFSUSHI.COM_-500x707.png')

    def is_going_to_hiragana_dakuon(self, event):
        text = event.message.text
        return text.lower() == 'hiragana_dakuon'

    def on_enter_hiragana_dakuon(self, event):
        send_text_message(event.reply_token, 'Display The hiragana_dakuon')

    def is_going_to_hiragana_combo(self, event):
        text = event.message.text
        return text.lower() == 'hiragana_combo'

    def on_enter_hiragana_combo(self, event):
        send_text_message(event.reply_token, 'Display The hiragana_combo')

    def is_going_to_hiragana_smallnlongvowels(self, event):
        text = event.message.text
        return text.lower() == 'hiragana_smallnlongvowels'

    def on_enter_hiragana_smallnlongvowels(self, event):
        send_text_message(event.reply_token, 'Display The hiragana_smallnlongvowels')

    def is_going_to_katakana_basic(self, event):
        text = event.message.text
        return text.lower() == 'basic'

    def on_enter_katakana_basic(self, event):
        send_image_message(event.reply_token, 'https://apieceofsushi.com/wp-content/uploads/2020/09/KatakanaChartBlackAPIECEOFSUSHI.COM_.png')

    def is_going_to_katakana_dakuon(self, event):
        text = event.message.text
        return text.lower() == 'dakuon'

    def on_enter_katakana_dakuon(self, event):
        send_text_message(event.reply_token, 'Display The Katakana_dakuon')

    def is_going_to_katakana_combo(self, event):
        text = event.message.text
        return text.lower() == 'combo'

    def on_enter_katakana_combo(self, event):
        send_text_message(event.reply_token, 'Display The katakana_combo')

    def is_going_to_katakana_smallnlongvowels(self, event):
        text = event.message.text
        return text.lower() == 'smallnlongvowels'

    def on_enter_katakana_smallnlongvowels(self, event):
        send_text_message(event.reply_token, 'Display The katakana_smallnlongvowels')

