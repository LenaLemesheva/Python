from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackContext
import sqlite3


bot_token = '5782309281:AAGR51gqRpEe8aCrqrIEN37JIgEn2THOqGY'
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher


conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()

def start(update: Update, context: CallbackContext):
    context.bot.send_message(update.effective_chat.id, f'Привет! Это phonebook!\n'
        f'Покажите абоненты /show_list\n' 
        f'Выберите абонент /record_search\n' 
        f'Добавьте абонент /add_subscriber\n' 
        f'Удалите абонент /delete_subscriber\n' 
        f'Обновите данные /change_data\n')
    return ConversationHandler.END


def show_list(update: Update, context: CallbackContext):
    cursor.execute('выберите * из числа абонентов')
    results = cursor.fetchall()
    update.message.reply_text(results)
    return (results)


def record_search(update: Update, context: CallbackContext):
    surname = 'Иванов'
    cursor.execute(f"выберите * абонент, фамилия которго '%{surname}%'")
    results = cursor.fetchall()
    update.message.reply_text(results)
    return (results)


def add_subscriber(update: Update, context: CallbackContext):
    name = 'Степан'
    surname = 'Степанов'
    phone = 888888
    description = 'сосед'
    cursor.execute(
        f"добавить (name, surname, phone, description) "
        f"величину ('{name}', '{surname}', {phone}, '{description}')")
    conn.commit()
    update.message.reply_text(conn)
    return conn

    
def delete_subscriber(update: Update, context: CallbackContext):
    id = 5
    cursor.execute(f"удалить из списка абонентов, где id={id}")
    conn.commit()
    update.message.reply_text(conn)
    return conn

    
def change_data(update: Update, context: CallbackContext):
    id = 3
    cursor.execute(f"изменить имя абонента ='Юрий' где id={id}")
    conn.commit()
    conn.close()
    update.message.reply_text(conn)
    return conn
  

start_handler = CommandHandler('start', start)
show_list_handler = CommandHandler('show_list', show_list)
record_search_handler = CommandHandler('record_search', record_search)
add_subscriber_handler = CommandHandler('add_subscriber', add_subscriber)
delete_subscriber_handler = CommandHandler('delete_subscriber', delete_subscriber)
change_data_handler = CommandHandler('change_data', change_data)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(show_list_handler)
dispatcher.add_handler(record_search_handler)
dispatcher.add_handler(add_subscriber_handler)
dispatcher.add_handler(delete_subscriber_handler)
dispatcher.add_handler(change_data_handler)
updater.start_polling()
updater.idle()  