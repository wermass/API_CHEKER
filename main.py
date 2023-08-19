import time
import requests
import telebot

API_URL = ''
TOKEN = ''
CHAT_ID = 0

bot = telebot.TeleBot(TOKEN)


def check_api():
    try:
        response = requests.get(API_URL)
        if response.status_code != 200:
            raise Exception(f"API {response.status_code}: {response.text}")
    except Exception as e:
        bot.send_message(CHAT_ID, f"Ошибка API: {e}")


if __name__ == '__main__':
    while True:
        check_api()
        time.sleep(60)
