from telebot import TeleBot
import requests
import json
from config import TOKEN, API

bot = TeleBot(TOKEN)
api = API

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Напиши название города:')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().capitalize()
    result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
    if result.status_code == 200:
        data = json.loads(result.text)
        temperature = (data["main"]["temp"])
        feels_like = (data["main"]['feels_like'])
        humidity = (data["main"]["humidity"])
        pressure = (data["main"]["pressure"])
        wind = (data["wind"]["speed"])
        smile = '🔥' if temperature > 20.0 else '🧊'
        bot.reply_to(message, f'Сейчас погода: {temperature}{smile}\nОщущается как: {feels_like}{smile}\n'
                              f'Влажность: {humidity}%💧\nДавление {pressure}💠\nВетер: {wind}м/с💨')

    else:
        bot.reply_to(message, "Город не существует")

bot.polling(none_stop=True)