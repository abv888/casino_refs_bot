class Localization:
    def __init__(
            self,
            push: str):
        self.push = push


PUSHES_MINUTES = {
    "en":"⚡️Bonus will be active only for next 24 hours⚡️\n\n"
         "Hurry up and take your bonus🎁",
    "pl":"⚡️Bonus będzie aktywny tylko przez następne 24 godziny⚡️\n\n"
         "Pospiesz się i odbierz swój bonus🎁",
    "esp":"⚡️El bono estará activo solo por las próximas 24 horas⚡️\n\n"
          "Apresúrate y reclama tu bono🎁",
    "cz":"⚡️Bonus bude aktivní pouze následujících 24 hodin⚡️\n\n"
         "Pospěšte si a vezměte si svůj bonus🎁",
    "it":"⚡️Il bonus sarà attivo solo per le prossime 24 ore⚡️\n\n"
         "Affrettati e prendi il tuo bonus🎁",
    "lt":"⚡️Bonuss būs aktīvs tikai nākamās 24 stundas⚡️\n\n"
         "Pasteidzies un paņem savu bonusu🎁",
    "french":"⚡️Le bonus sera actif uniquement pour les 24 prochaines heures⚡️\n\n"
         "Dépêchez-vous et prenez votre bonus🎁",
    "dutch":"⚡️Bonus vil være aktivt kun i de næste 24 timer⚡️\n\n"
            "Skynd dig og tag din bonus🎁",
    "tr":"⚡️Bonus sadece önümüzdeki 24 saat boyunca aktif olacak⚡️\n\n"
         "Hemen harekete geç ve bonusunu al🎁",
    "rom":"⚡️Bonusul va fi activ doar pentru următoarele 24 de ore⚡️\n\n"
          "Grăbește-te și ia-ți bonusul🎁",
    "prt":"⚡️O bônus estará ativo apenas pelas próximas 24 horas⚡️\n\n"
          "Apressa-te e pega teu bônus🎁",
    "de":"⚡️Der Bonus ist nur für die nächsten 24 Stunden aktiv⚡️\n\n"
         "Beeil dich und hol dir deinen Bonus🎁",
    "ru":"⚡️Бонус будет активен только в течение следующих 24 часов⚡️\n\n"
         "Поторопитесь и заберите свой бонус🎁",

}

PUSHES_DAY = {
    "en":"️⚡️Your personal bonus will expire in 30 minutes ⚡️\n\n"
         "Hurry up and pick your bonus🎁",
    "pl":"⚡️Twój osobisty bonus wygaśnie za 30 minut ⚡️\n\n"
         "Pospiesz się i odbierz swój bonus 🎁",
    "esp":"⚡️Tu bono personal expirará en 30 minutos ⚡️\n\n"
          "Apresúrate y reclama tu bono 🎁",
    "cz":"⚡️Váš osobní bonus vyprší za 30 minut ⚡️\n\n"
         "Pospěšte si a vyzvedněte si svůj bonus 🎁",
    "it":"⚡️Il tuo bonus personale scadrà tra 30 minuti ⚡️\n\n"
         "Affrettati e prendi il tuo bonus 🎁",
    "lt":"⚡️Jūsu personīgais bonuss beigsies pēc 30 minūtēm ⚡️\n\n"
         "Pasteidzieties un paņemiet savu bonusu 🎁",
    "french":"⚡️Votre bonus personnel expirera dans 30 minutes ⚡️\n\n"
         "Dépêchez-vous et prenez votre bonus 🎁",
    "dutch":"⚡️Din personlige bonus udløber om 30 minutter ⚡️\n\n"
            "Skynd dig og hent din bonus 🎁",
    "tr":"⚡️Kişisel bonusunuz 30 dakika içinde sona erecek ⚡️\n\n"
         "Hemen harekete geç ve bonusunu al 🎁",
    "rom":"⚡️Bonusul tău personal va expira în 30 de minute ⚡️\n\n"
          "Grăbește-te și ia-ți bonusul 🎁",
    "prt":"⚡️Seu bônus pessoal expirará em 30 minutos ⚡️\n\n"
          "Apressa-te e pega teu bônus 🎁",
    "de":"⚡️Dein persönlicher Bonus läuft in 30 Minuten ab ⚡️\n\n"
         "Beeil dich und hol dir deinen Bonus 🎁",
    "ru":"⚡️Ваш личный бонус истечет через 30 минут ⚡️\n\n"
         "Поторопитесь и заберите свой бонус 🎁",

}