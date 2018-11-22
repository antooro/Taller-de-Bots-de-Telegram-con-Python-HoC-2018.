import telebot


bot = telebot.TeleBot("785998722:AAFE5BalhP1IqjB4gTxJN80qHp1Cp-S0imI")
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    m = message.from_user.first_name
    if message.from_user.last_name is not None: m+=message.from_user.last_name
    bot.reply_to(message,m )
bot.polling()