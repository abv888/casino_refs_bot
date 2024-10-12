import asyncio
import telebot.async_telebot as telebot
from telebot import types
import os
from dotenv import (
    load_dotenv,
    find_dotenv
)

load_dotenv(
    find_dotenv()
)

bot = telebot.AsyncTeleBot(
    token=os.getenv("BOT_TOKEN")
)
ADMIN_ID = os.getenv("ADMIN_1")

@bot.message_handler(commands=['start', 'menu'])
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
        espana_button = types.InlineKeyboardButton(
            text="España 🇪🇸",
            callback_data="espana"
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
            espana_button,
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
            url="https://www.youtube.com/"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/1xslots.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 1XSLOTS - ¡el mejor proyecto para los jugadores de 🇲🇽 México! \n\n"
                 "🚀 ¡Recoge tu paquete de bienvenida con 100 giros gratis y un bono del 100% en tu depósito!\n\n"
                 "👉 Ventajas del 1XSLOTS Casino: \n"
                 "⚡️ Bonos diarios\n"
                 "⚡️ Alto RTP\n"
                 "⚡️ Cajas de botín con premios increíbles\n"
                 "⚡️ MUCHOS BONOS SIN DEPÓSITO\n\n"
                 "Haz clic en el botón de abajo y empieza a jugar 👇",
            reply_markup=keyboard
        )
    elif call.data == "peru":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🔥 Recir bono 🔥",
            url="https://www.youtube.com/"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/1xslots.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 1XSLOTS - ¡el mejor proyecto para los jugadores de 🇵🇪 Perú! \n\n"
                 "🚀 ¡Recoge tu paquete de bienvenida con 100 giros gratis y un bono del 100% en tu depósito!\n\n"
                 "👉 Ventajas del 1XSLOTS Casino: \n"
                 "⚡️ Bonos diarios\n"
                 "⚡️ Alto RTP\n"
                 "⚡️ Cajas de botín con premios increíbles\n"
                 "⚡️ MUCHOS BONOS SIN DEPÓSITO\n\n"
                 "Haz clic en el botón de abajo y empieza a jugar 👇",
            reply_markup=keyboard
        )
    elif call.data == "chile":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🔥 Recir bono 🔥",
            url="https://www.youtube.com/"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/1xslots.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 1XSLOTS - ¡el mejor proyecto para los jugadores de 🇨🇱 Chile! \n\n"
                 "🚀 ¡Recoge tu paquete de bienvenida con 100 giros gratis y un bono del 100% en tu depósito!\n\n"
                 "👉 Ventajas del 1XSLOTS Casino: \n"
                 "⚡️ Bonos diarios\n"
                 "⚡️ Alto RTP\n"
                 "⚡️ Cajas de botín con premios increíbles\n"
                 "⚡️ MUCHOS BONOS SIN DEPÓSITO\n\n"
                 "Haz clic en el botón de abajo y empieza a jugar 👇",
            reply_markup=keyboard
        )
    elif call.data == "ecuador":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🔥 Recir bono 🔥",
            url="https://www.youtube.com/"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/1xslots.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 1XSLOTS - ¡el mejor proyecto para los jugadores de 🇪🇨 Ecuador! \n\n"
                 "🚀 ¡Recoge tu paquete de bienvenida con 100 giros gratis y un bono del 100% en tu depósito!\n\n"
                 "👉 Ventajas del 1XSLOTS Casino: \n"
                 "⚡️ Bonos diarios\n"
                 "⚡️ Alto RTP\n"
                 "⚡️ Cajas de botín con premios increíbles\n"
                 "⚡️ MUCHOS BONOS SIN DEPÓSITO\n\n"
                 "Haz clic en el botón de abajo y empieza a jugar 👇",
            reply_markup=keyboard
        )
    elif call.data == "espana":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="Registro 😎",
            url="https://www.youtube.com/"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/casino_infinity_espana.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 Únete a CasinoInfinity\n\n"
                 "⚡️ Paquete de bienvenida: 100% en el depósito + 200 giros gratis\n\n"
                 "Beneficios de CasinoInfinity:\n"
                 "🔥 Alto RTP\n"
                 "🔥 Bono de recarga de fin de semana: 700 EUR + 50 giros gratis\n"
                 "🔥 Cashback en vivo: 25% hasta 200 EUR\n"
                 "🔥 Programa VIP\n"
                 "🔥 Muchos bonos\n\n"
                 "Haz clic en el botón de abajo para registrarte y obtener tu bono 👇",
            reply_markup=keyboard
        )
    elif call.data == "other_esp":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🔥 Recir bono 🔥",
            url="https://www.youtube.com/"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/1xslots.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 1XSLOTS - ¡el mejor proyecto para los jugadores de América Latina! \n\n"
                 "🚀 ¡Recoge tu paquete de bienvenida con 100 giros gratis y un bono del 100% en tu depósito!\n\n"
                 "👉 Ventajas del 1XSLOTS Casino: \n"
                 "⚡️ Bonos diarios\n"
                 "⚡️ Alto RTP\n"
                 "⚡️ Cajas de botín con premios increíbles\n"
                 "⚡️ MUCHOS BONOS SIN DEPÓSITO\n\n"
                 "Haz clic en el botón de abajo y empieza a jugar 👇",
            reply_markup=keyboard
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
            url="https://redirspinner.com/2gLd?p=%2Fregistration%2F"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/spinbetter.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 Bgaming tarafından Aztec Clusters'da 250 ücretsiz dönüş kazanın\n\n"
                 "Yapmanız gerekenler:\n"
                 "⭐️ SPINBETTER'a kaydolun\n"
                 "⭐️ Promosyon kodunu girin: AZTEC200 (kayıt sonrası)\n\n"
                 "Promosyon kodunu nerede girmeli?\n"
                 "⚡️ Mobil Sürüm: Profil > Promosyonlar > Casino VIP Cashback > Bonuslar\n"
                 "⚡️ PC Sürümü: Profil > Bonuslar ve Hediyeler\n\n"
                 "SPINBETTER'in Avantajları:\n"
                 "🔥 Hoşgeldin paketi 56927 TL + 150 Ücretsiz Dönüş\n"
                 "🔥 Yüksek RTP\n"
                 "🔥 Sadakat programı\n"
                 "🔥 Pek çok bonus",
            reply_markup=keyboard
        )
    elif call.data == "fr":
        keyboard = types.InlineKeyboardMarkup(
            row_width=2
        )
        france_button = types.InlineKeyboardButton(
            text="France 🇫🇷",
            callback_data="france"
        )
        senegal_button = types.InlineKeyboardButton(
            text="Sénégal 🇸🇳",
            callback_data="senegal"
        )
        cameroun_button = types.InlineKeyboardButton(
            text="Cameroun 🇨🇲",
            callback_data="cameroun"
        )
        cotdivoir_button = types.InlineKeyboardButton(
            text="Côte d'Ivoire 🇨🇮",
            callback_data="cotdivoir"
        )
        benin_button = types.InlineKeyboardButton(
            text="Bénin 🇧🇯",
            callback_data="benin"
        )
        autres_button = types.InlineKeyboardButton(
            text="Autres pays",
            callback_data="autres"
        )
        keyboard.add(
            france_button,
            senegal_button,
            cameroun_button,
            cotdivoir_button,
            benin_button,
            autres_button
        )
        await bot.send_message(
            chat_id=call.message.chat.id,
            text="Choisir un pays:",
            reply_markup=keyboard
        )
    elif call.data == "france":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🚀 Activer le bonus 🚀",
            url="https://www.youtube.com/"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/luckyhunter.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 Rejoignez LuckyHunter !\n\n"
                    "🔥 Code promo : LUCKY \n"
                    "Obtenez 444 free spins et 25000 EUR!\n\n"
                    "✨ Cashback quotidien jusqu'à 15 %\n"
                    "✨ 7 % de bonus sur tous les dépôts en crypto\n"
                    "✨ RTP élevé\n"
                    "✨ Programme VIP TOP\n"
                    "✨ Bonus de rechargement\n\n"
                    "Réclamez votre bonus maintenant 👇👇👇",
            reply_markup=keyboard
        )
    elif call.data == "senegal":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🚀 S'inscrire 🚀",
            url="https://www.youtube.com/"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/betwinner.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 Rejoignez BetWinner !\n\n"
                    "🔥 Profite de ton pack de bienvenue : 150 tours gratuits + 200% sur ton dépôt\n\n"
                    "✨ RTP élevé\n"
                    "✨ Programme VIP TOP\n"
                    "✨ Bonus de rechargement\n\n"
                    "Réclamez votre bonus maintenant 👇👇👇",
            reply_markup=keyboard
        )
    elif call.data == "cameroun":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🚀 S'inscrire 🚀",
            url="https://www.youtube.com/"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/betwinner.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 Rejoignez BetWinner !\n\n"
                    "🔥 Profite de ton pack de bienvenue : 150 tours gratuits + 200% sur ton dépôt\n\n"
                    "✨ RTP élevé\n"
                    "✨ Programme VIP TOP\n"
                    "✨ Bonus de rechargement\n\n"
                    "Réclamez votre bonus maintenant 👇👇👇",
            reply_markup=keyboard
        )
    elif call.data == "cotdivoir":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🚀 S'inscrire 🚀",
            url="https://www.youtube.com/"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/betwinner.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 Rejoignez BetWinner !\n\n"
                    "🔥 Profite de ton pack de bienvenue : 150 tours gratuits + 200% sur ton dépôt\n\n"
                    "✨ RTP élevé\n"
                    "✨ Programme VIP TOP\n"
                    "✨ Bonus de rechargement\n\n"
                    "Réclamez votre bonus maintenant 👇👇👇",
            reply_markup=keyboard
        )
    elif call.data == "benin":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🚀 S'inscrire 🚀",
            url="https://www.youtube.com/"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/betwinner.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 Rejoignez BetWinner !\n\n"
                    "🔥 Profite de ton pack de bienvenue : 150 tours gratuits + 200% sur ton dépôt\n\n"
                    "✨ RTP élevé\n"
                    "✨ Programme VIP TOP\n"
                    "✨ Bonus de rechargement\n\n"
                    "Réclamez votre bonus maintenant 👇👇👇",
            reply_markup=keyboard
        )
    elif call.data == "autres":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        take_bonus_button = types.InlineKeyboardButton(
            text="🚀 S'inscrire 🚀",
            url="https://www.youtube.com/"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/betwinner.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 Rejoignez BetWinner !\n\n"
                    "🔥 Profite de ton pack de bienvenue : 150 tours gratuits + 200% sur ton dépôt\n\n"
                    "✨ RTP élevé\n"
                    "✨ Programme VIP TOP\n"
                    "✨ Bonus de rechargement\n\n"
                    "Réclamez votre bonus maintenant 👇👇👇",
            reply_markup=keyboard
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
            url="https://www.youtube.com/"
        )
        keyboard.add(
            take_bonus_button
        )
        await bot.send_photo(
            photo=open(f"resources/auf.jpg", "rb"),
            chat_id=call.message.chat.id,
            caption="😎 Залетай в казино AUF\n\n"
            "✨ До 20% кешбека\n"
            "✨ До 300% и 500 FS на первый депозит\n"
            "✨ Нет лимитов на вывод\n"
            "✨ Крутая программа лояльности, где нужно раздевать девушек 😜\n\n"
            "Забирай свой бонус 👇👇👇",
            reply_markup=keyboard
        )

async def main():
    await bot.polling(
        none_stop=True
    )

asyncio.run(main())