import telebot
from queue import Queue

photos = Queue()

bot = telebot.TeleBot("785998722:AAFE5BalhP1IqjB4gTxJN80qHp1Cp-S0imI")



@bot.message_handler(content_types=['photo'])
def store_photo(message):
    photos.put(message.photo[1].file_id)
    

@bot.message_handler(commands=['get'])
def get_photo(message):
    photo_id = photos.get()
    bot.send_photo(message.chat.id , photo_id)

bot.polling()
