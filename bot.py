import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import aiocron
import telebot.async_telebot as telebot
from sqlalchemy.ext.asyncio import AsyncSession
from telebot import types
import os
from dotenv import (
    load_dotenv,
    find_dotenv
)
load_dotenv(
    find_dotenv()
)

from db.engine import (
    session_maker,
    drop_db,
    create_db
)

from db.engine import session_maker
from db.models import User
from db.requests import add_user, get_user_by_id, get_all_users


bot = telebot.AsyncTeleBot(
    token=os.getenv("BOT_TOKEN")
)

@bot.message_handler(commands=['start'])
async def start(message):
    async with session_maker() as session:
        if await get_user_by_id(
            session=session,
            user_id=message.from_user.id
        ) is None:
            user = User(
                telegram_id=message.from_user.id,
                full_name=message.from_user.full_name,
                username=message.from_user.username
            )
            await add_user(
                session=session,
                user=user,
            )
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
        callback_data="lt"
    )
    bl_button = types.InlineKeyboardButton(
        text="Belgium 🇧🇪",
        callback_data="bl"
    )
    tr_button = types.InlineKeyboardButton(
        text="Türkçe 🇹🇷",
        callback_data="tr"
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
        pl_button,
        esp_button,
        cz_button,
        it_button,
        lt_button,
        bl_button,
        tr_button,
        rom_button,
        prt_button,
        de_button,
        ru_button
    )
    await bot.send_message(
        chat_id=message.chat.id,
        text="Select language / Выберите язык",
        reply_markup=keyboard
    )
    # Отправка сообщения через 15 минут
    await asyncio.sleep(900)
    await bot.send_message(
        chat_id=message.chat.id,
        text="⚡️Bonus will be active only for next 24 hours⚡️\n\n"
             "Hurry up and take your bonus🎁"
    )

async def send_daily_notification():
    async with session_maker() as session:
        users = await get_all_users(session)  # Получаем всех пользователей
        for user in users:
            await bot.send_message(
                chat_id=user.telegram_id,
                text="⚡️Bonus will be active only for next 24 hours⚡️\n\n"
                     "Hurry up and take your bonus🎁"
            )

# Функция для ежедневной рассылки в 18:00
# @aiocron.crontab('49 1 * * *')  # cron-синтаксис для ежедневной рассылки в 18:00
# async def send_daily_message():
#     async with session_maker() as session:
#         users = await get_all_users(session)  # Получаем всех пользователей
#         for user in users:
#             await bot.send_message(
#                 chat_id=user.telegram_id,
#                 text="⚡️Bonus will be active only for next 24 hours⚡️\n\n"
#                      "Hurry up and take your bonus🎁"
#             )

@bot.message_handler(commands=['menu'])
async def menu(message):
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
        callback_data="lt"
    )
    bl_button = types.InlineKeyboardButton(
        text="Belgium 🇧🇪",
        callback_data="bl"
    )
    tr_button = types.InlineKeyboardButton(
        text="Türkçe 🇹🇷",
        callback_data="tr"
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
        pl_button,
        esp_button,
        cz_button,
        it_button,
        lt_button,
        bl_button,
        tr_button,
        rom_button,
        prt_button,
        de_button,
        ru_button
    )
    await bot.send_message(
        chat_id=message.chat.id,
        text="Select language / Выберите язык",
        reply_markup=keyboard
    )

@bot.callback_query_handler(
    func=lambda call:True
)
async def callback_inline(call):
    if call.data == "en":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🚀 Take a BONUS 🚀",
            url="https://redirspinner.com/2gLd?p=%2Fregistration%2F"
        )
        next_casino_button = types.InlineKeyboardButton(
            text="Next casino 😎",
            callback_data="en_verde"
        )
        keyboard.add(
            take_bonus_button,
            next_casino_button
        )
        await bot.send_photo(
            photo=open(f"resources/spinbetter.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="🤑Grab 250 no-deposit free spins in Aztec Clusters by Bgaming\n\n"
                 "Here’s what you need to do: \n"
                 "⚡️Sign up at SPINBETTER \n"
                 "⚡️Enter the promo code  (after registration) \n\n"
                 "Where to enter the promo code?\n"
                 "⚡️ Mobile Version: Profile > Promo > Casino VIP Cashback > Bonuses\n"
                 "⚡️PC Version: Profile > Bonuses & Gifts\n\n"
                 "Benefits of SPINBETTER: \n"
                 "🔥 Welcome package 1500 EUR + 150 FS \n"
                 "🔥 High RTP \n"
                 "🔥 Loyalty program \n"
                 "🔥 A lot of Bonuses\n",
            reply_markup=keyboard
        )
    elif call.data == "en_verde":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🚀 Take a BONUS 🚀",
            url="https://verdepromo.com/l/6709b0e11751796bf80eb19a"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/verde.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 Get 50 no-deposit free spins for signing up at VERDE Casino!\n\n"
              "Here's how to claim your free spins: \n"
              "⚡️ Register at VERDE Casino \n"
              "⚡️ Confirm your email and phone number \n"
              "⚡️ Complete account verification\n\n"
              "Benefits of VERDE Casino: \n"
              "🔥 Welcome package of 1200 EUR + 220 free spins \n"
              "🔥 High RTP \n"
              "🔥 Excellent loyalty program \n"
              "🔥 Lotteries and tournaments \n"
              "🔥 Sportsbook\n\n"
              "Click the button below to register and claim your bonus 👇",
            reply_markup=keyboard
        )
    elif call.data == "pl":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🚀 Zgarnij BONUS 🚀",
            url="https://redirspinner.com/2gLd?p=%2Fregistration%2F"
        )
        next_casino_button = types.InlineKeyboardButton(
            text="Następne kasyno 😎",
            callback_data="pl_hitnspin"
        )
        keyboard.add(
            take_bonus_button,
            next_casino_button
        )
        await bot.send_photo(
            photo=open(f"resources/spinbetter.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 Zgarnij 250 darmowych spinów bez depozytu w grze Aztec Clusters by Bgaming\n\n"
                        "Co musisz zrobić:\n"
                        "⭐️ Zarejestruj się na SPINBETTER\n"
                        "⭐️ Wpisz kod promocyjny AZTEC200 (po rejestracji)\n\n"
                        "Gdzie wpisać kod promocyjny?\n"
                        "⚡️ Wersja mobilna: Profil > Promocje > Casino VIP Cashback > Bonusy\n"
                        "⚡️ Wersja na PC: Profil > Bonusy i Prezenty\n\n"
                        "Korzyści z SPINBETTER:\n"
                        "🔥 Pakiet powitalny 6000 PLN + 150 darmowych spinów\n"
                        "🔥 Wysokie RTP\n"
                        "🔥 Program lojalnościowy\n"
                        "🔥 Mnóstwo bonusów\n",
            reply_markup=keyboard
        )
    elif call.data =="pl_hitnspin":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🚀 Zgarnij BONUS 🚀",
            url="https://hitnspinpromo.com/l/6709b15f82cfae76b3030d70"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/hitnspin_pl.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 50 darmowych spinów bez depozytu za rejestrację w Hit'n'Spin Casino!\n\n"
                     "Co musisz zrobić, aby odebrać darmowe spiny:\n"
                     "🔥 Zarejestruj się w Hit'n'Spin Casino\n"
                     "🔥 Potwierdź e-mail i numer telefonu\n"
                     "🔥 Zweryfikuj swoje konto\n"
                     "🔥 Wejdź do gry Big Bass Splash\n\n"
                     "Zalety Hit'n'Spin Casino:\n"
                     "🚀 Pakiet powitalny 3500 PLN + 200 darmowych spinów\n"
                     "🚀 Wysokie RTP\n"
                     "🚀 Świetny program lojalnościowy\n"
                     "🚀 Loterie i turnieje\n"
                     "🚀 Zakłady sportowe\n\n"
                     "Kliknij przycisk poniżej, aby zarejestrować się i odebrać swój bonus 👇",
            reply_markup=keyboard
        )
    elif call.data == "esp":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        mexico_button = types.InlineKeyboardButton(
            text="México 🇲🇽",
            callback_data="mexico"
        )
        peru_button = types.InlineKeyboardButton(
            text="Peru 🇵🇪",
            callback_data="peru"
        )
        chile_button = types.InlineKeyboardButton(
            text="Chile 🇨🇱",
            callback_data="chile"
        )
        ecuador_button = types.InlineKeyboardButton(
            text="Ecuador 🇪🇨",
            callback_data="ecuador"
        )
        other_esp_button = types.InlineKeyboardButton(
            text="Otro país",
            callback_data="other_esp"
        )
        keyboard.add(
            mexico_button,
            peru_button,
            chile_button,
            ecuador_button,
            other_esp_button
        )
        await bot.send_message(
            chat_id=call.message.chat.id,
            text="Elige tu país 👇",
            reply_markup=keyboard
        )
    elif call.data == "mexico":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🔥 Recir bono 🔥",
            url="https://1wseqo.life/v3/aggressive-casino?p=nj92"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/1win_esp.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="Únete a 1WIN\n\n" \
                    "⚡️Retiros rápidos a tarjetas de cualquier país \n" \
                    "⚡️No se requiere verificación de documentos🪪\n" \
                    "⚡️No hay límites de edad🙅\n" \
                    "⚡️Bono de bienvenida del <b><i>500%</i></b> en tu primer depósito \n\n" \
                    "Promoción - <b>BGGW</b>",
            reply_markup=keyboard,
            parse_mode="HTML"
        )
    elif call.data == "peru":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🔥 Recir bono 🔥",
            url="https://1wseqo.life/v3/aggressive-casino?p=nj92"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/1win_esp.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="Únete a 1WIN\n\n" \
                    "⚡️Retiros rápidos a tarjetas de cualquier país \n" \
                    "⚡️No se requiere verificación de documentos🪪\n" \
                    "⚡️No hay límites de edad🙅\n" \
                    "⚡️Bono de bienvenida del <b><i>500%</i></b> en tu primer depósito \n\n" \
                    "Promoción - <b>BGGW</b>",
            reply_markup=keyboard,
            parse_mode="HTML"
        )
    elif call.data == "chile":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🔥 Recir bono 🔥",
            url="https://1wseqo.life/v3/aggressive-casino?p=nj92"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/1win_esp.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="Únete a 1WIN\n\n" \
                    "⚡️Retiros rápidos a tarjetas de cualquier país \n" \
                    "⚡️No se requiere verificación de documentos🪪\n" \
                    "⚡️No hay límites de edad🙅\n" \
                    "⚡️Bono de bienvenida del <b><i>500%</i></b> en tu primer depósito \n\n" \
                    "Promoción - <b>BGGW</b>",
            reply_markup=keyboard,
            parse_mode="HTML"
        )
    elif call.data == "ecuador":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🔥 Recir bono 🔥",
            url="https://1wseqo.life/v3/aggressive-casino?p=nj92"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/1win_esp.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="Únete a 1WIN\n\n" \
                    "⚡️Retiros rápidos a tarjetas de cualquier país \n" \
                    "⚡️No se requiere verificación de documentos🪪\n" \
                    "⚡️No hay límites de edad🙅\n" \
                    "⚡️Bono de bienvenida del <b><i>500%</i></b> en tu primer depósito \n\n" \
                    "Promoción - <b>BGGW</b>",
            reply_markup=keyboard,
            parse_mode="HTML"
        )
    elif call.data == "other_esp":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🔥 Recir bono 🔥",
            url="https://1wseqo.life/v3/aggressive-casino?p=nj92"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/1win_esp.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="Únete a 1WIN\n\n" \
                    "⚡️Retiros rápidos a tarjetas de cualquier país \n" \
                    "⚡️No se requiere verificación de documentos🪪\n" \
                    "⚡️No hay límites de edad🙅\n" \
                    "⚡️Bono de bienvenida del <b><i>500%</i></b> en tu primer depósito \n\n" \
                    "Promoción - <b>BGGW</b>",
            reply_markup=keyboard,
            parse_mode="HTML"
        )
    elif call.data == "cz":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🚀 Vyxvednout bonus 🚀",
            url="https://redirspinner.com/2gLd?p=%2Fregistration%2F"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/spinbetter.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 Získejte 250 bezplatných zatočení bez vkladu ve hře Aztec Clusters by Bgaming\n\n"
                 "Co musíte udělat:\n"
                 "⭐️ Zaregistrujte se na SPINBETTER\n"
                 "⭐️ Zadejte promo kód AZTEC200 (po registraci)\n\n"
                 "Kde zadat promo kód?\n"
                 "⚡️ Mobilní verze: Profil > Promo > Casino VIP Cashback > Bonusy\n"
                 "⚡️ Verze pro PC: Profil > Bonusy a Dárky\n\n"
                 "Výhody SPINBETTER:\n"
                 "🔥 Uvítací balíček 1500 EUR + 150 bezplatných zatočení\n"
                 "🔥 Vysoké RTP\n"
                 "🔥 Věrnostní program\n"
                 "🔥 Spousta bonusů",
            reply_markup=keyboard
        )
    elif call.data == "it":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🚀 Riscatta il bonus 🚀",
            url="https://redirspinner.com/2gLd?p=%2Fregistration%2F"
        )
        next_casino_button = types.InlineKeyboardButton(
            text="Il prossimo casinó 😎",
            callback_data="it_verde"
        )
        keyboard.add(
            take_bonus_button,
            next_casino_button
        )
        await bot.send_photo(
            photo=open(f"resources/spinbetter.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 Ottieni 250 giri gratis senza deposito in Aztec Clusters di Bgaming\n\n"
                 "Ecco cosa devi fare: \n"
                 "⭐️ Iscriviti su SPINBETTER \n"
                 "⭐️ Inserisci il codice promo AZTEC200 (dopo la registrazione)\n\n"
                 "Dove inserire il codice promo? \n"
                 "⚡️ Versione Mobile: Profilo > Promo > VIP Cashback Casino > Bonus \n\n"
                 "⚡️ Versione PC: Profilo > Bonus e Regali\n\n"
                 "Vantaggi di SPINBETTER: \n"
                 "🔥 Pacchetto di benvenuto 1500 EUR + 150 giri gratis \n"
                 "🔥 Alto RTP \n"
                 "🔥 Programma fedeltà \n"
                 "🔥 Tanti Bonus",
            reply_markup=keyboard
        )
    elif call.data == "it_verde":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🚀 Iscriviti e ottieni il bonus 🚀",
            url="https://verdepromo.com/l/6709b0e11751796bf80eb19a"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/verde.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 50 giri gratis senza deposito per la registrazione su VERDE Casino!\n\n"
                 "Cosa fare per ottenere i giri gratis:\n"
                 "⚡️ Registrati su VERDE Casino\n"
                 "⚡️ Conferma la tua email e il numero di telefono\n"
                 "⚡️ Completa la verifica dell'account\n\n"
                 "I vantaggi di VERDE Casino:\n"
                 "🔥 Pacchetto di benvenuto 1200 EUR + 220 giri gratis\n"
                 "🔥 Alto RTP\n"
                 "🔥 Ottimo programma fedeltà\n"
                 "🔥 Lotterie e tornei\n"
                 "🔥 Sportsbook\n\n"
                 "Clicca sul pulsante qui sotto per registrarti e ottenere il tuo bonus 👇",
            reply_markup=keyboard
        )
    elif call.data == "lt":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🚀 Paņem bonusu 🚀",
            url="https://redirspinner.com/2gLd?p=%2Fregistration%2F"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/spinbetter.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 Paņem 250 bezdepozīta bezmaksas griezienus spēlē Aztec Clusters by Bgaming\n\n"
                 "Lūk, kas tev jādara:\n"
                 "⭐️ Reģistrējies SpinBetter\n"
                 "⭐️ Ievadi promo kodu AZTEC200 (pēc reģistrācijas)\n\n"
                 "Kur ievadīt promo kodu?\n"
                 "⚡️ Mobilā versija: Profils > Promo > Casino VIP Cashback > Bonusi\n"
                 "⚡️ Datora versija: Profils > Bonusi un dāvanas\n\n"
                 "SpinBetter priekšrocības:\n"
                 "🔥 Iepazīšanās bonuss līdz 1500 EUR + 150 bezmaksas griezieni\n"
                 "🔥 Augsts RTP\n"
                 "🔥 Lojalitātes programma\n"
                 "🔥 Daudz bonusu",
            reply_markup=keyboard
        )
    elif call.data == "bl":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        dutch_button = types.InlineKeyboardButton(
            text="Dutch 🇳🇱",
            callback_data="dutch"
        )
        french_button = types.InlineKeyboardButton(
            text="French 🇫🇷",
            callback_data="french"
        )
        german_button = types.InlineKeyboardButton(
            text="German 🇩🇪",
            callback_data="german"
        )
        keyboard.add(
            dutch_button,
            french_button,
            german_button
        )
        await bot.send_message(
            chat_id=call.message.chat.id,
            text="Choose your language:",
            reply_markup=keyboard
        )
    elif call.data == "dutch":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🚀 Bonus ophalen 🚀",
            url="https://redirspinner.com/2gLd?p=%2Fregistration%2F"
        )
        next_casino_button = types.InlineKeyboardButton(
            text="Het volgende casino 😎",
            callback_data="dutch_hitnspin"
        )
        keyboard.add(
            take_bonus_button,
            next_casino_button
        )
        await bot.send_photo(
            photo=open(f"resources/spinbetter.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 Pak 250 gratis spins zonder storting in Aztec Clusters by Bgaming\n\n"
                 "Dit moet je doen om je gratis spins te krijgen: \n"
                 "⭐️ Meld je aan bij SPINBETTER \n"
                 "⭐️ Voer de promotiecode AZTEC200 in na registratie\n\n"
                 "Waar de promotiecode invoeren? \n"
                 "⚡️ Mobiele versie: Profiel > Promo > Casino VIP Cashback > Bonussen \n"
                 "⚡️ PC-versie: Profiel > Bonussen & Geschenken\n\n"
                 "Voordelen van SPINBETTER: \n"
                 "🔥 Welkomstpakket: 1500 EUR + 150 gratis spins \n"
                 "🔥 Hoge RTP \n"
                 "🔥 Loyaliteitsprogramma \n"
                 "🔥 Veel bonussen",
            reply_markup=keyboard
        )
    elif call.data == "dutch_hitnspin":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="⚡️ Registreer je en ontvang de bonus ⚡️",
            url="https://hitnspinpromo.com/l/6709b15f82cfae76b3030d70"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/hitnspin_en.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 50 gratis spins zonder storting voor registratie bij Hit'n'Spin Casino!\n\n"
                 "Wat moet je doen om je gratis spins te ontvangen: \n"
                 "🔥 Registreer je bij Hit'n'Spin Casino \n"
                 "🔥 Bevestig je e-mail en telefoonnummer \n"
                 "🔥 Verifieer je account \n"
                 "🔥 Start het spel Big Bass Splash\n\n"
                 "Voordelen van Hit'n'Spin Casino: \n"
                 "🚀 Welkomstpakket van 800 EUR + 200 gratis spins \n"
                 "🚀 Hoge RTP \n"
                 "🚀 Geweldig loyaliteitsprogramma \n"
                 "🚀 Loterijen en toernooien \n"
                 "🚀 Sportweddenschappen\n\n"
                 "Klik op de knop hieronder om je te registreren en je bonus te ontvangen 👇",
            reply_markup=keyboard
        )
    elif call.data == "french":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🚀 Obtenz votre bonus 🚀",
            url="https://redirspinner.com/2gLd?p=%2Fregistration%2F"
        )
        next_casino_button = types.InlineKeyboardButton(
            text="Le prochain casino 😎",
            callback_data="french_hitnspin"
        )
        keyboard.add(
            take_bonus_button,
            next_casino_button
        )
        await bot.send_photo(
            photo=open(f"resources/spinbetter.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 Obtenez 250 tours gratuits sans dépôt dans Aztec Clusters by Bgaming\n\n"
                 "Voici ce que vous devez faire pour recevoir vos tours gratuits :\n"
                 "⭐️ Inscrivez-vous sur SPINBETTER\n"
                 "⭐️ Entrez le code promo AZTEC200 après l'inscription\n\n"
                 "Où entrer le code promo ?\n"
                 "⚡️ Version mobile : Profil > Promo > Casino VIP Cashback > Bonus\n"
                 "⚡️ Version PC : Profil > Bonus & Cadeaux\n\n"
                 "Avantages de SPINBETTER :\n"
                 "🔥 Pack de bienvenue : 1500 EUR + 150 tours gratuits\n"
                 "🔥 RTP élevé\n"
                 "🔥 Programme de fidélité\n"
                 "🔥 De nombreux bonus",
            reply_markup=keyboard
        )
    elif call.data == "french_hitnspin":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="⚡️ Inscris-toi et réclame ton bonus ⚡️",
            url="https://hitnspinpromo.com/l/6709b15f82cfae76b3030d70"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/hitnspin_fr.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 50 tours gratuits sans dépôt pour votre inscription au Hit'n'Spin Casino !\n\n"
                 "Voici ce que vous devez faire pour obtenir vos tours gratuits :\n"
                 "🔥 Inscrivez-vous au Hit'n'Spin Casino\n"
                 "🔥 Confirmez votre e-mail et votre numéro de téléphone\n"
                 "🔥 Vérifiez votre compte\n"
                 "🔥 Lancez le jeu Big Bass Splash\n\n"
                 "Avantages du Hit'n'Spin Casino :\n"
                 "🚀 Offre de bienvenue : 800 EUR + 200 tours gratuits\n"
                 "🚀 RTP élevé\n"
                 "🚀 Excellent programme de fidélité\n"
                 "🚀 Loteries et tournois\n"
                 "🚀 Paris sportifs\n\n"
                 "Cliquez sur le bouton ci-dessous pour vous inscrire et obtenir votre bonus 👇",
            reply_markup=keyboard
        )
    elif call.data == "german":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🚀 Bonus holen 🚀",
            url="https://redirspinner.com/2gLd?p=%2Fregistration%2F"
        )
        next_casino_button = types.InlineKeyboardButton(
            text="Das nächste Casino 😎",
            callback_data="german_hitnspin"
        )
        keyboard.add(
            take_bonus_button,
            next_casino_button
        )
        await bot.send_photo(
            photo=open(f"resources/spinbetter.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 Hol dir 250 Freispiele ohne Einzahlung in Aztec Clusters by Bgaming\n\n"
                 "Das musst du tun, um deine Freispiele zu erhalten:\n"
                 "⭐️ Melde dich bei SPINBETTER an\n"
                 "⭐️ Gib nach der Registrierung den Promo-Code AZTEC200 ein\n\n"
                 "Wo den Promo-Code eingeben?\n"
                 "⚡️ Mobile Version: Profil > Promo > Casino VIP Cashback > Boni\n"
                 "⚡️ PC-Version: Profil > Boni & Geschenke\n\n"
                 "Vorteile von SPINBETTER:\n"
                 "🔥 Willkommenspaket: 1500 EUR + 150 Freispiele\n"
                 "🔥 Hohe RTP\n"
                 "🔥 Treueprogramm\n"
                 "🔥 Viele Boni",
            reply_markup=keyboard
        )
    elif call.data == "german_hitnspin":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="⚡️ Registriere dich und hol dir den Bonus ⚡️",
            url="https://hitnspinpromo.com/l/6709b15f82cfae76b3030d70"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/hitnspin_de.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 50 Freispiele ohne Einzahlung für die Registrierung im Hit'n'Spin Casino!\n\n"
                 "Was musst du tun, um deine Freispiele zu erhalten: \n"
                 "🔥 Registriere dich im Hit'n'Spin Casino 🔥 Bestätige deine E-Mail und Telefonnummer \n"
                 "🔥 Verifiziere dein Konto \n"
                 "🔥 Starte das Spiel Big Bass Splash\n\n"
                 "Vorteile des Hit'n'Spin Casinos: \n"
                 "🚀 Willkommenspaket von 800 EUR + 200 Freispiele \n"
                 "🚀 Hohe RTP \n"
                 "🚀 Großartiges Treueprogramm \n"
                 "🚀 Lotterien und Turniere \n"
                 "🚀 Sportwetten\n\n"
                 "Klicke auf den Button unten, um dich zu registrieren und deinen Bonus zu erhalten 👇",
            reply_markup=keyboard
        )
    elif call.data == "tr":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🚀 Bonusu AI 🚀",
            url="https://1wbpqg.top/v3/aggressive-casino?p=ho99"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/1win_tr.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="1WIN'e Katıl\n\n" \
                    "⚡️Herhangi bir ülkenin kartına hızlı para çekme \n" \
                    "⚡️Belge doğrulaması gerekli değil🪪\n" \
                    "⚡️Yaş sınırı yok🙅\n" \
                    "⚡️Hoşgeldin Bonusu <b><i>%500</i></b> para yatırma bonusu \n\n" \
                    "Promosyon - <b>BGGW</b>",
        reply_markup=keyboard,
        parse_mode="HTML"
        )
    elif call.data == "rom":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🚀 Revendică bonusul 🚀",
            url="https://redirspinner.com/2gLd?p=%2Fregistration%2F"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/spinbetter.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 Ia 250 de rotiri gratuite fără depunere în Aztec Clusters by Bgaming\n\n"
                 "Iată ce trebuie să faci:\n"
                 "⭐️ Înscrie-te la SPINBETTER\n"
                 "⭐️ Introdu codul promoțional AZTEC200 (după înregistrare)\n\n"
                 "Unde să introduci codul promoțional?\n"
                 "⚡️ Versiune Mobilă: Profil > Promo > Casino VIP Cashback > Bonusuri\n"
                 "⚡️ Versiune PC: Profil > Bonusuri & Cadouri\n\n"
                 "Beneficiile SPINBETTER:\n"
                 "🔥 Pachet de bun venit 1500 EUR + 150 FS\n"
                 "🔥 RTP ridicat\n"
                 "🔥 Program de loialitate\n"
                 "🔥 O mulțime de bonusuri",
            reply_markup=keyboard
        )
    elif call.data == "prt":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🚀 Resgatar Bõnus 🚀",
            url="https://redirspinner.com/2gLd?p=%2Fregistration%2F"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/spinbetter.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 Ganhe 250 giros grátis sem depósito em Aztec Clusters by Bgaming\n\n"
                 "Veja o que você precisa fazer:\n"
                 "⭐️ Cadastre-se no SPINBETTER\n"
                 "⭐️ Insira o código promocional AZTEC200 (após o registro)\n\n"
                 "Onde inserir o código promocional?\n"
                 "⚡️ Versão Mobile: Perfil > Promo > Casino VIP Cashback > Bônus\n"
                 "⚡️ Versão para PC: Perfil > Bônus e Presentes\n\n"
                 "Benefícios do SPINBETTER:\n"
                 "🔥 Pacote de boas-vindas de 1500 EUR + 150 giros grátis\n"
                 "🔥 Alto RTP\n"
                 "🔥 Programa de Fidelidade\n"
                 "🔥 Muitos Bônus",
            reply_markup=keyboard
        )
    elif call.data == "de":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🚀 Bonus holen 🚀",
            url="https://redirspinner.com/2gLd?p=%2Fregistration%2F"
        )
        next_casino_button = types.InlineKeyboardButton(
            text="Das nächste Casino 😎",
            callback_data="de_hitnspin"
        )
        keyboard.add(
            take_bonus_button,
            next_casino_button
        )
        await bot.send_photo(
            photo=open(f"resources/spinbetter.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 Hol dir 250 Freispiele ohne Einzahlung in Aztec Clusters by Bgaming\n\n"
                 "Das musst du tun, um deine Freispiele zu erhalten:\n"
                 "⭐️ Melde dich bei SPINBETTER an\n"
                 "⭐️ Gib nach der Registrierung den Promo-Code AZTEC200 ein\n\n"
                 "Wo den Promo-Code eingeben?\n"
                 "⚡️ Mobile Version: Profil > Promo > Casino VIP Cashback > Boni\n"
                 "⚡️ PC-Version: Profil > Boni & Geschenke\n\n"
                 "Vorteile von SPINBETTER:\n"
                 "🔥 Willkommenspaket: 1500 EUR + 150 Freispiele\n"
                 "🔥 Hohe RTP\n"
                 "🔥 Treueprogramm\n"
                 "🔥 Viele Boni",
            reply_markup=keyboard
        )
    elif call.data == "de_hitnspin":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="⚡️ Registriere dich und hol dir den Bonus ⚡️",
            url="https://hitnspinpromo.com/l/6709b15f82cfae76b3030d70"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/hitnspin_de.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 50 Freispiele ohne Einzahlung für die Registrierung im Hit'n'Spin Casino!\n\n"
                 "Was musst du tun, um deine Freispiele zu erhalten: \n"
                 "🔥 Registriere dich im Hit'n'Spin Casino 🔥 Bestätige deine E-Mail und Telefonnummer \n"
                 "🔥 Verifiziere dein Konto \n"
                 "🔥 Starte das Spiel Big Bass Splash\n\n"
                 "Vorteile des Hit'n'Spin Casinos: \n"
                 "🚀 Willkommenspaket von 800 EUR + 200 Freispiele \n"
                 "🚀 Hohe RTP \n"
                 "🚀 Großartiges Treueprogramm \n"
                 "🚀 Lotterien und Turniere \n"
                 "🚀 Sportwetten\n\n"
                 "Klicke auf den Button unten, um dich zu registrieren und deinen Bonus zu erhalten 👇",
            reply_markup=keyboard
        )
    elif call.data == "ru":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🚀 Забрать бонус 🚀",
            url="https://1warlo.top/casino/list?open=register&p=nwk8"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/1win_ru.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="Заходи на 1WIN\n\n"
                    "⚡️Быстрый вывод на карту любой страны \n"
                    "⚡️Не требуется подтверждение документов🪪\n"
                    "⚡️Нет возрастных ограничений🙅\n"
                    "⚡️Приветсвенный бонус <b><i>500%</i></b> к пополнению \n\n"
                    "Промо - <b>BGGW</b>",
            reply_markup=keyboard,
            parse_mode="HTML"
        )

async def on_startup():
    scheduler.start()
    run_param = False
    if run_param:
        await drop_db()

    await create_db()

scheduler = AsyncIOScheduler()
scheduler.add_job(send_daily_notification, "cron", day_of_week="mon-sun", hour=18, minute=0)

async def main():
    await on_startup()
    await bot.polling(
        none_stop=True
    )

asyncio.run(main())