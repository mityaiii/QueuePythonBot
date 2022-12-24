import time
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.callback_data import CallbackData

names_of_subject = ['Алгоритмы', 'Основы Программирования']

primary_id = [i for i in open('list_of_group/primary_info.txt').read().split()]
TOKEN = primary_id[0]
primary_id.pop(0)
number_of_person = 30
number_of_button_in_row = 5

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
cb = CallbackData('post', 'msg_text')
primary_id = [0] * 30

class User:
    info_about_user = {'user_id' : "", 'user_first_name' : "", 'user_full_name' : ""}
    root_mode = False 

user = User()

def get_info_about_user(message: types.Message) -> None:
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_full_name = message.from_user.full_name

    user.info_about_user['user_id'] = user_id
    user.info_about_user['user_first_name'] = user_first_name
    user.info_about_user['user_full_name'] = user_full_name

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message) -> None:
    get_info_about_user(message=message)
    
    greetings_text = f"Привет, {user.info_about_user['user_first_name']}!"

    button_help = types.KeyboardButton(text="Помощь")
    button_choose_subject = types.KeyboardButton(text="Записаться в очередь")

    start_markup = types.ReplyKeyboardMarkup()
    start_markup.add(button_help, button_choose_subject)

    await bot.send_message(chat_id=message.from_user.id, text=greetings_text, reply_markup=start_markup)

def write_in_file(subject, number_in_queue) -> str:
    file_with_queue = open("list_of_group/{subject}.txt")
    file_with_queue

def get_info_from_file(subject):
    file_with_queue = open("list_of_group/{subject}.txt")
    content = file_with_queue.read().split('\n')
    return content

# Делал так, чтобы нельзя было записаться в очередь много раз
# Необходимо добавить возможность отписаться и считывание из файла  
@dp.callback_query_handler(cb.filter())
async def pressed_button(call: types.CallbackQuery, callback_data: dict) -> None:
    await call.answer()
    number_of_button = int(callback_data['msg_text']) - 1
    subject = call.message.text.split('\n')[0]

    info_from_file = get_info_from_file(subject=subject)

    if call.message.from_user.id in accepted_queue:
        await bot.send_message(chat_id=call.message.chat.id, text='Для того, чтобы занять очередь, нужно освободить место')
    else:
        new_markup = call.message.reply_markup
        new_markup.inline_keyboard[number_of_button // number_of_button_in_row][number_of_button % number_of_button_in_row].text = f'{number_of_button + 1}❌'
        new_markup = call.message.text.split('\n')
        new_text[number_of_button + 1] = f'{number_of_button + 1}. {user.info_about_user["user_first_name"]}'
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, text=new_text, reply_markup=new_markup)

@dp.message_handler()
async def action_handler(message: types.Message) -> None:
    text_with_subject = 'Subject\n'
    for i in range(number_of_person):
        text_with_subject += f'{i + 1}.\n'
    if message.text in names_of_subject:
        text_with_subject = message.text
        buttons = []    
        markup_with_queue = types.InlineKeyboardMarkup(row_width=number_of_button_in_row)

        for i in range(number_of_person):
            buttons.append(types.InlineKeyboardButton(text=f'{i + 1}✅', callback_data=cb.new(msg_text=f'{i + 1}')))
        markup_with_queue.add(*buttons)

        await bot.send_message(chat_id=message.from_user.id, text=text_with_subject, reply_markup=markup_with_queue)
    elif message.text == 'Записаться в очередь':
        buttons = []
        for name in names_of_subject:
            buttons.append(types.KeyboardButton(text=name))
        buttons.append(types.KeyboardButton(text='Вернуться в главное меню'))

        markup_with_subject = types.ReplyKeyboardMarkup()
        markup_with_subject.add(*buttons)

        await bot.send_message(chat_id=message.from_user.id, text='Выберите предмет', reply_markup=markup_with_subject)
    elif message.text == 'Вернуться в главное меню':
        await start_handler(message=message)

if __name__ == '__main__':
    executor.start_polling(dp)