
# -*- encoding: utf-8 -*-

import logging
from django.conf import settings
from ...models import Users, Items, PaymentHistory, Profiles, ReferalBase
from ...kb import inlinekb
from ...TextConfig import Texts as textconf
from ...TextConfig import Links as link

import telebot
from telebot import types

from django.core.management.base import BaseCommand

bot = telebot.TeleBot(token=settings.TOKEN_BOT)

logging.basicConfig(level=logging.INFO)

class Command(BaseCommand):
    help = 'bot'

    def handle(self, *args, **options):
        return ''

def check_user(id, username):
    account, _ = Users.objects.get_or_create(
        external_id=id,
        defaults={
            'username': username
        }
    )
    refbase, _ = ReferalBase.objects.get_or_create(
        external_id=id
    )
    profile, _ = Profiles.objects.get_or_create(
        external_id=id
    )

def pay_refer(chat, cost):
    r = ReferalBase.objects.get(external_id=chat).from_who
    if bool(r):
        profile_referer = Profiles.objects.get(external_id=r)
        profile_referer.wallet = int(profile_referer.wallet) + ((int(cost)//100)*10)//100
        profile_referer.save()
        s_r = ReferalBase.objects.get(external_id=r).from_who
        if bool(s_r):
            profile_sub_referer = Profiles.objects.get(external_id=s_r)
            profile_sub_referer.wallet = int(profile_sub_referer.wallet) + ((int(cost)//100)*5)//100
            profile_sub_referer.save()

def check_refer(deep, chat):
    r = bool(ReferalBase.objects.filter(external_id=deep))
    if r:
        l = ReferalBase.objects.get(external_id=chat)
        if l.from_who:
            bot.send_message(chat, textconf.refer_dump)
        else:
            l.from_who = deep
            l.save()
            listt = ReferalBase.objects.get(external_id=deep)
            ref = Users.objects.get(external_id=chat)
            listt.referals.add(ref)
            listt.save()
            c = Profiles.objects.get(external_id=deep)
            c.ref_count = c.ref_count + 1
            c.save()
            cs = ReferalBase.objects.get(external_id=deep).from_who
            if bool(cs):
                csf = Profiles.objects.get(external_id=cs)
                csf.sub_ref_count = csf.sub_ref_count + 1
                csf.save()
    else:
        bot.send_message(chat_id=chat, text=textconf.errormes)

def check_sub_channel(chat):
    if link.channel is None:
        return True
    else:
        try:
            chat_member = bot.get_chat_member(chat_id='@' + link.channel, user_id=chat)
            if chat_member.status != 'left':
                return True
            else:
                return False
        except Exception as e:
            return False


# Создать GraphQL query #
def user_profile(chat):
    data_ref = Profiles.objects.get(external_id=chat).ref_count
    data_sub_ref = Profiles.objects.get(external_id=chat).sub_ref_count
    data_cells_all = Profiles.objects.get(external_id=chat).cells_count
    data_cells_occupied = Profiles.objects.get(external_id=chat).cells_occupied
    data_team_all = Profiles.objects.get(external_id=chat).team_volume
    data_team_occupied = Profiles.objects.get(external_id=chat).team_occupied
    data_chats = Profiles.objects.get(external_id=chat).chats
    data_wallet = Profiles.objects.get(external_id=chat).wallet
    block = {
        'ref_count': data_ref,
        'sub_ref_count': data_sub_ref,
        'cells_count': data_cells_all,
        'cells_occupied': data_cells_occupied,
        'team_volume': data_team_all,
        'team_occupied': data_team_occupied,
        'chats': data_chats,
        'wallet': data_wallet
    }
    # res = data_item, data_ref, data_sub_ref, data_wallet
    return block

def items_name():
    names_list = Items.objects.values_list('name', flat=True)
    return names_list

def items_data(name):
    price = Items.objects.get(name=name).price
    description = Items.objects.get(name=name).description
    volume = Items.objects.get(name=name).volume
    pack = types.LabeledPrice(label=name, amount=price)
    res = description, pack, volume
    return res

def up_volume(chat, volume):
    vol = Profiles.objects.get(external_id=chat)
    vol.items_count = int(vol.items_count) + int(volume)
    vol.save()

def create_transaction(chat, cost):
    trans = PaymentHistory(external_id=chat, summ=cost)
    trans.save()

def get_start_link(chat):
    bot_u = bot.get_me()
    aff_link = f'https://t.me/{bot_u.username}?start={chat}'
    return aff_link

@bot.message_handler(commands=['start'])
def welcome(message: types.Message):
    try:
        chat = message.chat.id
        kb = inlinekb.homekb(message)
        kb_decline_q = inlinekb.check_subkb_allf(message)
        kb_decline_w = inlinekb.check_subkb_ct(message)
        check_user(message.chat.id, message.chat.username)
        if " " in message.text:
            try:
                deep = message.text.split()[1]
                deep = int(deep)
                if chat != deep:
                    check_refer(deep, message.chat.id)
                else:
                    bot.send_message(chat, textconf.refererr)
            except ValueError:
                bot.send_message(chat, textconf.bad_deep)
        if check_sub_channel(chat):
            bot.send_message(chat, textconf.welcomemes.format(
                firstname=message.chat.first_name
            ), reply_markup=kb)
        else:
            bot.send_message(chat, textconf.channel_invite, reply_markup=kb_decline_w)
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, textconf.errormes)

# 
# @bot.pre_checkout_query_handler(lambda query: True)
# def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
#     bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
# 
# @bot.message_handler(content_types=['successful_payment'])
# def process_successful_payment(message: types.Message):
#     pmnt = message.successful_payment
#     chat = message.successful_payment.telegram_payment_charge_id.split('_')[1]
#     price = pmnt.total_amount
#     item_volume = pmnt.invoice_payload
#     create_transaction(chat, price)
#     pay_refer(chat, price)
#     up_volume(chat, item_volume)
#     d = types.ReplyKeyboardRemove()
#     kb = inlinekb.homekb(chat)
#     bot.send_message(chat, textconf.successful_payment.format(
#         total_amount=price//100,
#         currency=pmnt.currency),
#                      reply_markup=d)
#     bot.send_message(chat, textconf.startmessage, reply_markup=kb)
# 
@bot.callback_query_handler(lambda call: True)
def callback_check(call: types.CallbackQuery):
    if call.data == 'check_sub':
        kb = inlinekb.homekb(call.data)
        kb_decline_w = inlinekb.check_subkb_ct(call.data)
        chat = call.message.chat.id
        if check_sub_channel(chat):
            bot.edit_message_text(chat_id=chat, message_id=call.message.id, text=textconf.welcomemes.format(
                firstname=call.message.chat.first_name
            ), reply_markup=kb)
        else:
            bot.edit_message_text(message_id=call.message.id, chat_id=chat,
                                  text=textconf.sub_decline + textconf.channel_invite, reply_markup=kb_decline_w)

    if call.data == 'home':
        chat = call.message.chat.id
        kb_decline_w = inlinekb.check_subkb_ct(call.data)
        if check_sub_channel(chat):
            kb = inlinekb.homekb(call.data)
            bot.edit_message_text(message_id=call.message.id, chat_id=chat,
                                  text=textconf.welcomemes, reply_markup=kb)
        else:
            bot.edit_message_text(message_id=call.message.id, chat_id=chat,
                                  text=textconf.sub_decline + textconf.channel_invite, reply_markup=kb_decline_w)

    if call.data == 'get_profile':
        kb_decline_w = inlinekb.check_subkb_ct(call.data)
        chat = call.message.chat.id
        if check_sub_channel(chat):
            data = user_profile(chat)
            kb = inlinekb.profilekb(call.data)
            bot.edit_message_text(message_id=call.message.id, chat_id=chat,
                                  text=textconf.profiletext.format(
                                            username=call.message.chat.username,
                                            team_occupied=data['team_occupied'],
                                            team_volume=data['team_volume'],
                                            cells=data['cells_count'],
                                            cells_occupied=data['cells_occupied'],
                                            chats=data['chats'],
                                            refcount=data['ref_count'],
                                            subrefcount=data['sub_ref_count'],
                                            balance=data['wallet']),
                                  reply_markup=kb)
        else:
            bot.edit_message_text(message_id=call.message.id, chat_id=chat,
                                  text=textconf.sub_decline + textconf.channel_invite, reply_markup=kb_decline_w)

    if call.data == 'make_send':
        kb_decline_w = inlinekb.check_subkb_ct(call.data)
        chat = call.message.chat.id
        if check_sub_channel(chat):
            kb = inlinekb.make_send_kb(call.data)
            data = user_profile(chat)
            bot.edit_message_text(message_id=call.message.id, chat_id=chat,
                                  text=textconf.sendinstuct.format(
                                      mescount=data[0]),
                                  reply_markup=kb)
        else:
            bot.edit_message_text(message_id=call.message.id, chat_id=chat,
                                  text=textconf.sub_decline + textconf.channel_invite, reply_markup=kb_decline_w)

    # if call.data == 'shop':
        kb_decline_w = inlinekb.check_subkb_ct(call.data)
        chat = call.message.chat.id
        if check_sub_channel(chat):
            kb = inlinekb.shopkb(call.data)
            bot.send_message(chat, textconf.choose, reply_markup=kb)
            names = items_name()
            for i in names:
                nick = i
                item_data = items_data(nick)
                bot.send_invoice(
                    call.message.chat.id,
                    title=nick,
                    description=item_data[0],
                    provider_token=settings.PAYMENT_TOKEN_YOO,
                    currency='rub',
                    is_flexible=False, 
                    prices=[item_data[1]],
                    start_parameter=item_data[2],
                    invoice_payload=item_data[2])
        else:
            bot.edit_message_text(message_id=call.message.id, chat_id=chat,
                                  text=textconf.sub_decline + textconf.channel_invite, reply_markup=kb_decline_w)

    if call.data == 'about':
        kb_decline_w = inlinekb.check_subkb_ct(call.data)
        chat = call.message.chat.id
        if check_sub_channel(chat):
            kb = inlinekb.aboutkb(call.data)
            bot.edit_message_text(message_id=call.message.id, chat_id=chat,
                                  text=textconf.abouttext, reply_markup=kb)
        else:
            bot.edit_message_text(message_id=call.message.id, chat_id=chat,
                                  text=textconf.sub_decline + textconf.channel_invite, reply_markup=kb_decline_w)

    if call.data == 'support':
        kb_decline_w = inlinekb.check_subkb_ct(call.data)
        chat = call.message.chat.id
        if check_sub_channel(chat):
            kb = inlinekb.supportkb(call.data)
            bot.edit_message_text(message_id=call.message.id, chat_id=chat,
                                  text=textconf.supporttext, reply_markup=kb)
        else:
            bot.edit_message_text(message_id=call.message.id, chat_id=chat,
                                  text=textconf.sub_decline + textconf.channel_invite, reply_markup=kb_decline_w)

    if call.data == 'partners':
        kb_decline_w = inlinekb.check_subkb_ct(call.data)
        chat = call.message.chat.id
        if check_sub_channel(chat):
            data = user_profile(chat)
            referal_link = get_start_link(chat)
            kb = inlinekb.parnerkb(call.data)
            bot.edit_message_text(message_id=call.message.id, chat_id=chat,
                                  text=textconf.partertext.format(
                                      refcount=data['ref_count'],
                                      subrefcount=data['sub_ref_count'],
                                      balance=data['wallet'],
                                      referal_link=referal_link),
                                  reply_markup=kb)
        else:
            bot.edit_message_text(message_id=call.message.id, chat_id=chat,
                                  text=textconf.sub_decline + textconf.channel_invite, reply_markup=kb_decline_w)

    if call.data == 'keep_money':
        kb_decline_w = inlinekb.check_subkb_ct(call.data)
        chat = call.message.chat.id
        if check_sub_channel(chat):
            kb = inlinekb.aboutkb(call.data)
            bot.edit_message_text(message_id=call.message.id, chat_id=chat,
                                  text=textconf.keep_money, reply_markup=kb)
        else:
            bot.edit_message_text(message_id=call.message.id, chat_id=chat,
                                  text=textconf.sub_decline + textconf.channel_invite_ct, reply_markup=kb_decline_w)

bot.polling(timeout=1)