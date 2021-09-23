"""Модуль Telegram Bot"""
import telebot


bot = telebot.TeleBot('2029649095:AAEI70MdGkaB56NeAQRyOqk8_A_osqvGHAQ')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    """Отлавливание сообщений пользователя и их обработка"""
    request = message.text.lower()
    response = 'Не понимаю'
    if request == '/start':
        response = 'Привет, я нейронная сеть :)\n*тут описание что я могу*'
    bot.send_message(message.from_user.id, response)


if __name__ == '__main__':
    bot.polling()
