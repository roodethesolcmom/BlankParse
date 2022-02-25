from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import emoji
from .TextConfig import Links as link

class inlinekb():
    def check_subkb_ct(self):
        kb = InlineKeyboardMarkup()
        b1 = InlineKeyboardButton(text='💬Подписаться', url=link.channel_url)
        b2 = InlineKeyboardButton(text='🔥Проверить подписку', callback_data='check_sub')
        res = kb.add(b1).add(b2)
        return res

    def homekb(self):
        kb = InlineKeyboardMarkup()
        b1 = InlineKeyboardButton(text=emoji.emojize(":bust_in_silhouette:")+"Профиль", callback_data='get_profile')
        b2 = InlineKeyboardButton(text=emoji.emojize(":check_mark_button:")+'Настройки', callback_data='settings')
        b3 = InlineKeyboardButton(text=emoji.emojize(":shopping_cart:")+'Маркет', callback_data='shop')
        # b4 = InlineKeyboardButton(text=emoji.emojize(":smiling_face_with_sunglasses:")+'О сервисе', callback_data='about')
        b5 = InlineKeyboardButton(text=emoji.emojize(":red_heart:")+'Тех поддержка', callback_data='support')
        b6 = InlineKeyboardButton(text=emoji.emojize(":bomb:")+'Спарсить БД'+emoji.emojize(":bomb:"), callback_data='parse_bd')
        # b7 = InlineKeyboardButton(text=emoji.emojize(":bell:")+'Отзывы', url=link.feedbacklink)
        res = kb.add(b2).add(b6).row(b1, b3).add(b5)
        return res

    def make_send_kb(self):
        kb = InlineKeyboardMarkup()
        b1 = InlineKeyboardButton(text=emoji.emojize(":high_voltage:")+"Новая ЦА",
                                  callback_data='new_aud')
        b2 = InlineKeyboardButton(text=emoji.emojize(":bust_in_silhouette:") + "Существующая ЦА",
                                  callback_data='my_aud')
        b3 = InlineKeyboardButton(text=emoji.emojize(":fire:") + "Наша ЦА" + emoji.emojize(":fire:"),
                                  callback_data='our_aud')
        b4 = InlineKeyboardButton(text=emoji.emojize(":shopping_cart:")+'Магазин', callback_data='shop')
        b5 = InlineKeyboardButton(text=emoji.emojize(":BACK_arrow:") + "Назад",
                                  callback_data='home')
        res = kb.row(b1, b2).add(b3).row(b4, b5)
        return res
    # Новая Ца

    # Существующая ца

    # Не\существующая Ца

    # Наша Ца

    # Категории

    # Подтверждение сообщения

    def profilekb(self):
        kb = InlineKeyboardMarkup()
        b1 = InlineKeyboardButton(text=emoji.emojize(":shopping_cart:") + 'Маркет', callback_data='shop')
        b2 = InlineKeyboardButton(text=emoji.emojize(":bomb:") + 'Партнерка', callback_data='partners')
        b3 = InlineKeyboardButton(text=emoji.emojize(":BACK_arrow:") + "Назад",
                                  callback_data='home')
        b4 = InlineKeyboardButton(text=emoji.emojize(":smiling_face_with_sunglasses:")+'О сервисе', callback_data='about')
        res = kb.row(b1, b4).add(b3).add(b4)
        return res

    def aboutkb(self):
        kb = InlineKeyboardMarkup()
        b1 = InlineKeyboardButton(text=emoji.emojize(":BACK_arrow:") + "Назад",
                                  callback_data='home')
        res = kb.add(b1)
        return res

    def supportkb(self):
        kb = InlineKeyboardMarkup()
        b1 = InlineKeyboardButton(text=emoji.emojize(":bust_in_silhouette:") + "Перейти в чат",
                                  url=link.supportlink)
        b2 = InlineKeyboardButton(text=emoji.emojize(":BACK_arrow:") + "Назад",
                                  callback_data='home')
        res = kb.add(b1, b2)
        return res

    def parnerkb(self):
        kb = InlineKeyboardMarkup()
        b2 = InlineKeyboardButton(text=emoji.emojize(":shopping_cart:") + 'Mаркет', callback_data='shop')
        b3 = InlineKeyboardButton(text=emoji.emojize(":BACK_arrow:") + "Назад",
                                  callback_data='home')
        res = kb.row(b2, b3)
        return res

    def shopkb(self):
        kb = ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = KeyboardButton(text=emoji.emojize(":confounded_face:") + "Домой" + emoji.emojize(":crying_cat:"))
        res = kb.add(b1)
        return res

    def shop(self, index, count):
        now = int(index)+1
        kb = InlineKeyboardMarkup()
        b_left = InlineKeyboardButton(text=emoji.emojize(":fast_reverse_button:"), callback_data='reverse_button')
        b_mid = InlineKeyboardButton(text=f'{now} / {count}')
        b_right = InlineKeyboardButton(text=emoji.emojize(":fast_forward_button:"), callback_data='forward_button')
        b_buy = InlineKeyboardButton(text=emoji.emojize(":fire:")+'Приобрести'+emoji.emojize(":fire:"), callback_data=f'buy_button {index}')
        b_gold = InlineKeyboardButton(text=emoji.emojize(":money_bag:")+'Купить Голду'+emoji.emojize(":money_bag:"), callback_data='buy_gold')
        b_back = InlineKeyboardButton(text=emoji.emojize(":BACK_arrow:")+'Назад в меню', callback_data='home')
        res = kb.row(b_left, b_mid, b_right).add(b_buy).add(b_gold).add(b_back)
        return res

