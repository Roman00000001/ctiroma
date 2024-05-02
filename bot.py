import telebot
import wikipedia

# Установка API токена
API_TOKEN = '7091011219:AAHjpWC_B86_j3vdPIGfBN4GM50pE7hUVBc'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я бот Романа, который поможет тебе найти информацию на Википедии. Просто отправь мне запрос.")

@bot.message_handler(func=lambda message: True)
def send_wiki_info(message):
    try:
        result = wikipedia.page(message.text)
        bot.send_message(message.chat.id, result.url)
    except wikipedia.exceptions.PageError:
        bot.send_message(message.chat.id, "По вашему запросу ничего не найдено.")
    except wikipedia.exceptions.DisambiguationError as e:
        options = ', '.join(e.options[:5])
        bot.send_message(message.chat.id, f"Не удалось найти точное совпадение. Возможные варианты: {options}.")

bot.polling()

