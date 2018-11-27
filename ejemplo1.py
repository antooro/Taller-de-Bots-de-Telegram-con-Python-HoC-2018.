import telebot
from queue import Queue


photos = Queue()
bot = telebot.TeleBot("785998722:AAFE5BalhP1IqjB4gTxJN80qHp1Cp-S0imI")

'''
lista = {}

@bot.message_handler(content_types=['photo'])
def store_photo(message):
    if not message.from_user.id in lista :
        photos = Queue()
        lista[message.from_user.id] = photos
    lista[message.from_user.id].put(message.photo[1].file_id)'''
@bot.message_handler(content_types=['photo'])
def store_photo(message):
    photos.put(message.photo[1].file_id)
    
'''@bot.message_handler(commands=["get"])
def get_photo(message):
    if message.from_user.id in lista :
        photo_id = lista[message.from_user.id].get()
        bot.send_photo(message.chat.id , photo_id)
    else:
        bot.send_message(message.chat.id, "No tienes nada en la cola")'''

'''@bot.message_handler(func=lambda message: message.from_user.username == 'antooro', commands=["get"])
def get_photo(message):
    photo_id = photos.get()
    bot.send_photo(message.chat.id , photo_id)'''

@bot.message_handler(commands=["get"])
def get_photo(message):
    photo_id = photos.get()
    bot.send_photo(message.chat.id , photo_id)

bot.polling()
