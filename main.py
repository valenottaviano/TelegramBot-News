import os
import telebot
from keep_alive import keep_alive 
from scrape_news import scrapeNews
from datetime import date

APY_KEY = os.environ['APY_KEY']
bot = telebot.TeleBot(APY_KEY)

@bot.message_handler(commands=['news'])
def news(message):
  news = scrapeNews()
  msg = []
  for new in news:
    msg.append(f"{new['title']}")
    msg.append(f"{new['href']}\n")
  
  msg.append(f"Última actualización: {date.today()}")
  bot.send_message(message.chat.id, '\n'.join(msg), disable_web_page_preview=True)

keep_alive()
bot.polling()