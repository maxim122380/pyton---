import telebot
import requests

token = "6695349813:AAEFSS0ZKKffmyumW0jQzGyTEcvd97OseNE"

bot = telebot.TeleBot(token)

def reqapi(ip):
    url = f"https://ipinfo.io/{ip}/geo"
    r = requests.get(url).json()
    return r

@bot.message_handler(commands=["start"])
def start(message):
    msg = bot.send_message(message.chat.id, f"hello,{message.from_user.username}\n Введи ip:")
    bot.register_next_step_handler(msg, getip)

def getip(message):
    ip = message.text
    res = str(reqapi(ip))
    bot.send_message(message.chat.id, res)

if __name__ == "__main__":
    bot.infinity_polling()