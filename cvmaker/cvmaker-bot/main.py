import telebot
from handlers_funcs import *
from initialize import bot
from flask import Flask, request
import os

server = Flask(__name__)
TOKEN = "5559451976:AAF6wpt7Ck1tElqGyk5xp6fUEgn5m2LlWJM"

@bot.message_handler(commands=['start'])
def welcome(msg):
    welcome_message(msg)

@bot.message_handler(commands=['edit', "about", "help"])
def edit_data(msg):
    bot.send_message(msg.chat.id, "هذه الاوامر غير متوفرة حاليا لأن هذه النسخة تجريبية")
    
# @bot.message_handler(commands=['help'])
# def help_message(msg):
#     bot.send_message(msg.chat.id, "يمكنك التواصل مع قسم الادارة والمبيعات :\n جوهر فراس @JR_21 \n او مع قسم التطوير والبرمجة : \n عبدالرحمن حسن @abdo_hss")
# 
# @bot.message_handler(commands=['about'])
# def about(msg):
#     bot.send_message(msg.chat.id, "The Smart Jober\n هو مشروع تنموي يهدف الى حل مشاكل البطالة وسوء اختيار الموظفين على حد سواء \n المشروع تابع لشبكة الجواهري التنموية بإدارة تنفيذية من \n جوهر فراس \n تم تطوير المشروع عن طريق فريق ProLancers \n للتواصل مع المطورين @abdo_hss \n\n شكر خاص لزين حمزة لمساهماته بالمشروع")
# 
@bot.message_handler(commands=['jober'])
def jober_message(msg):
    #job_sender(msg)
    bot.send_message(msg.chat.id, "هذه الميزة غير متاحة حاليا كونها تخضع للتحسين")                      

@bot.callback_query_handler(func=lambda call: call.data in "cb_example")
def example(call):
    example_messages(call)

@bot.callback_query_handler(func=lambda call: True)
def choices(call):
    user_chocies(call)


@bot.message_handler()
def info(msg):
    get_info(msg)

@bot.message_handler(content_types=['photo'])
def send_cv(msg):
    photo(msg)


@bot.callback_query_handler(lambda call: call.data in [edit_calls])
def editing(call):
    edit_info(call)

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

bot.remove_webhook()
bot.infinity_polling()

# @server.route("/")
# def webhook():
#     bot.remove_webhook()
#     bot.set_webhook(url='https://smart-jober.herokuapp.com/' + TOKEN)
#     return "HELLO, WORLD ! JOBER IS WORKING...", 200
# 
# 
# if __name__ == "__main__":
#     server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))