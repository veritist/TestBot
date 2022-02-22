import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    bot.forward_message(-647801647, message.chat.id, message.message_id)

if __name__ == '__main__':
     bot.polling(none_stop=True)