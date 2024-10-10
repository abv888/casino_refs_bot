import asyncio
import telebot.async_telebot as telebot
from telebot import types
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

bot = telebot.AsyncTeleBot(token=os.getenv("BOT_TOKEN"))
ADMIN_ID = os.getenv("ADMIN_1")

@bot.message_handler(commands=['start'])
async def start(message):
    keyboard = types.InlineKeyboardMarkup(
        row_width=2
    )
    en_button = types.InlineKeyboardButton(
        text="English 🇬🇧",
        callback_data="en"
    )
    ru_button = types.InlineKeyboardButton(
        text="Русский 🇷🇺",
        callback_data="ru"
    )
    nl_button = types.InlineKeyboardButton(
        text="Netherlands 🇳🇱",
        callback_data="nl"
    )
    pl_button = types.InlineKeyboardButton(
        text="Polski 🇵🇱",
        callback_data="pl"
    )
    it_button = types.InlineKeyboardButton(
        text="Italiano 🇮🇹",
        callback_data="it"
    )
    cz_button = types.InlineKeyboardButton(
        text="Český 🇨🇿",
        callback_data="cz"
    )
    esp_button = types.InlineKeyboardButton(
        text="Español 🇪🇸",
        callback_data="esp"
    )
    lt_button = types.InlineKeyboardButton(
        text="Latviešu 🇱🇻",
        callback_data="lv"
    )
    bl_button = types.InlineKeyboardButton(
        text="Belgium 🇧🇪",
        callback_data="bl"
    )
    tr_button = types.InlineKeyboardButton(
        text="Türkçe 🇹🇷",
        callback_data="tr"
    )
    fr_button = types.InlineKeyboardButton(
        text="Français 🇫🇷",
        callback_data="fr"
    )
    prt_button = types.InlineKeyboardButton(
        text="Português 🇵🇹",
        callback_data="prt"
    )
    rom_button = types.InlineKeyboardButton(
        text="Română 🇷🇴",
        callback_data="rom"
    )
    de_button = types.InlineKeyboardButton(
        text="Deutch 🇩🇪",
        callback_data="de"
    )
    keyboard.add(
        en_button,
        nl_button,
        pl_button,
        esp_button,
        cz_button,
        it_button,
        lt_button,
        bl_button,
        tr_button,
        fr_button,
        rom_button,
        prt_button,
        de_button,
        ru_button
    )
    await bot.send_message(chat_id=message.chat.id,
                           text="Select language / Выберите язык",
                           reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
async def callback_inline(call):
    if call.data == "en":
        ...
    elif call.data == "nl":
        ...
    elif call.data == "pl":
        ...
    elif call.data == "esp":
        ...
    elif call.data == "cz":
        ...
    elif call.data == "it":
        ...
    elif call.data == "lt":
        ...
    elif call.data == "bl":
        ...
    elif call.data == "tr":
        ...
    elif call.data == "fr":
        ...
    elif call.data == "rom":
        ...
    elif call.data == "prt":
        ...
    elif call.data == "de":
        ...
    elif call.data == "ru":
        ...

async def main():
    await bot.polling(none_stop=True)

asyncio.run(main())