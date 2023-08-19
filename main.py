import time
import requests
import telebot

API_URL = ''
TELEGRAM_TOKEN = ''
CHAT_ID_EVGEN = 149242583
CHAT_ID_WERMASS = 5124962240

bot = telebot.TeleBot(TELEGRAM_TOKEN)

SITE_IS_UP = True
MESSAGE_SENT = False


def check_api():
    global SITE_IS_UP, MESSAGE_SENT

    try:
        response = requests.get(API_URL)
        response.raise_for_status()

        if not SITE_IS_UP and not MESSAGE_SENT:
            bot.send_message(CHAT_ID_EVGEN, "Сайт ожил")
            bot.send_message(CHAT_ID_WERMASS, "Сайт ожил")
            SITE_IS_UP = True
            MESSAGE_SENT = True

        elif SITE_IS_UP and MESSAGE_SENT:
            MESSAGE_SENT = False

    except requests.RequestException:
        if SITE_IS_UP or not MESSAGE_SENT:
            bot.send_message(CHAT_ID_EVGEN, "Сайт упал")
            bot.send_message(CHAT_ID_WERMASS, "Сайт упал")
            SITE_IS_UP = False
            MESSAGE_SENT = True

        elif not SITE_IS_UP and MESSAGE_SENT:
            MESSAGE_SENT = False


if __name__ == '__main__':
    while True:
        check_api()
        time.sleep(60)
