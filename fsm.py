from transitions.extensions import GraphMachine

from linebot.models import MessageTemplateAction
from utils import send_text_message, send_button_message, send_image_message

#https://apieceofsushi.com/wp-content/uploads/2020/09/HiraganaChartPinkAPIECEOFSUSHI.COM_-500x707.png - hiragana https://japanesetactics.com/wp-content/uploads/2020/01/how-to-learn-hiragana.jpg
#https://apieceofsushi.com/wp-content/uploads/2020/09/KatakanaChartBlackAPIECEOFSUSHI.COM_.png - katakana https://japanesetactics.com/wp-content/uploads/2020/01/how-to-learn-katakana.jpg


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_user(self, event):
        text = event.message.text
        return text.lower() == 'back'

    def on_enter_user(self, event):
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
        url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Japanese_icon_%28for_user_box%29.svg/1024px-Japanese_icon_%28for_user_box%29.svg.png'
        send_button_message(event.reply_token, title, text, btn, url)

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
        url = 'https://www.japan-academy.in/blog/wp-content/uploads/2021/04/Difference-between-Hiragana-and-Katakana-in-Japanese-Language-870x600.jpg'
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_hiragana(self, event):
        text = event.message.text
        return text.lower() == 'hiragana'

    def on_enter_hiragana(self, event):
        title = 'Lets learn Japanese'
        text = 'Choose『Hiragana』Or『Katakana』'
        btn = [
            MessageTemplateAction(
                label='Basic',
                text='Basic'
            ),
            MessageTemplateAction(
                label='Dakuon',
                text='Dakuon'
            ),
            MessageTemplateAction(
                label='Combo',
                text='Combo'
            ),
            MessageTemplateAction(
                label='SL-Vowels',
                text='smallnlongvowels'
            ),
        ]
        url = 'https://japanesetactics.com/wp-content/uploads/2020/01/how-to-learn-hiragana.jpg'
        send_button_message(event.reply_token, title, text, btn, url)
        #send_text_message(event.reply_token, 'Choose『Basic』Or『Dakuon』Or『Combo』Or『SmallnLongVowels』')

    def is_going_to_katakana(self, event):
        text = event.message.text
        return text.lower() == 'katakana'

    def on_enter_katakana(self, event):
        title = 'Lets learn Japanese'
        text = 'Choose『Hiragana』Or『Katakana』'
        btn = [
            MessageTemplateAction(
                label='Basic',
                text='Basic'
            ),
            MessageTemplateAction(
                label='Dakuon',
                text='Dakuon'
            ),
            MessageTemplateAction(
                label='Combo',
                text='Combo'
            ),
            MessageTemplateAction(
                label='SL-Vowels',
                text='smallnlongvowels'
            ),
        ]
        url = 'https://japanesetactics.com/wp-content/uploads/2020/01/how-to-learn-katakana.jpg'
        send_button_message(event.reply_token, title, text, btn, url)
        #send_text_message(event.reply_token, 'Choose『Basic』Or『Dakuon』Or『Combo』Or『SmallnLongVowels』')

    def is_going_to_hiragana_basic(self, event):
        text = event.message.text
        return text.lower() == 'basic'

    def on_enter_hiragana_basic(self, event):
        send_image_message(event.reply_token, 'https://apieceofsushi.com/wp-content/uploads/2020/09/HiraganaChartPinkAPIECEOFSUSHI.COM_-500x707.png')
        send_text_message(event.reply_token, 'Type 『back』 to go back to main menu')

    def is_going_to_hiragana_dakuon(self, event):
        text = event.message.text
        return text.lower() == 'dakuon'

    def on_enter_hiragana_dakuon(self, event):
        send_image_message(event.reply_token, 'https://github.com/ChrisDeantana/TOC-LineBot/blob/master/img/H_dakuon.jpg?raw=true')
        send_text_message(event.reply_token, 'Type 『back』 to go back to main menu')

    def is_going_to_hiragana_combo(self, event):
        text = event.message.text
        return text.lower() == 'combo'

    def on_enter_hiragana_combo(self, event):
        send_image_message(event.reply_token, 'https://github.com/ChrisDeantana/TOC-LineBot/blob/master/img/H_combo.jpg?raw=true')
        send_text_message(event.reply_token, 'Type 『back』 to go back to main menu')

    def is_going_to_hiragana_smallnlongvowels(self, event):
        text = event.message.text
        return text.lower() == 'smallnlongvowels'

    def on_enter_hiragana_smallnlongvowels(self, event):
        send_image_message(event.reply_token, 'https://github.com/ChrisDeantana/TOC-LineBot/blob/master/img/H_smallnlongvowels.jpg?raw=true')
        send_text_message(event.reply_token, 'Type 『back』 to go back to main menu')

    def is_going_to_katakana_basic(self, event):
        text = event.message.text
        return text.lower() == 'basic'

    def on_enter_katakana_basic(self, event):
        send_image_message(event.reply_token, 'https://apieceofsushi.com/wp-content/uploads/2020/09/KatakanaChartBlackAPIECEOFSUSHI.COM_.png')
        send_text_message(event.reply_token, 'Type 『back』 to go back to main menu')

    def is_going_to_katakana_dakuon(self, event):
        text = event.message.text
        return text.lower() == 'dakuon'

    def on_enter_katakana_dakuon(self, event):
        send_image_message(event.reply_token, 'https://github.com/ChrisDeantana/TOC-LineBot/blob/master/img/K_dakuon.jpg?raw=true')
        send_text_message(event.reply_token, 'Type 『back』 to go back to main menu')

    def is_going_to_katakana_combo(self, event):
        text = event.message.text
        return text.lower() == 'combo'

    def on_enter_katakana_combo(self, event):
        send_image_message(event.reply_token, 'https://github.com/ChrisDeantana/TOC-LineBot/blob/master/img/K_combo.jpg?raw=true')
        send_text_message(event.reply_token, 'Type 『back』 to go back to main menu')

    def is_going_to_katakana_smallnlongvowels(self, event):
        text = event.message.text
        return text.lower() == 'smallnlongvowels'

    def on_enter_katakana_smallnlongvowels(self, event):
        send_image_message(event.reply_token, 'https://github.com/ChrisDeantana/TOC-LineBot/blob/master/img/K_smallnlongvowels.jpg?raw=true')
        send_text_message(event.reply_token, 'Type 『back』 to go back to main menu')

