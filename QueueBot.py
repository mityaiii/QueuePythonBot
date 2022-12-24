import Group
import FileManager

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.callback_data import CallbackData

TOKEN = open('list_of_group/primary_info.txt', 'r').read().split()[0]
root_id = [i for i in range(1, len(open('list_of_group/primary_info.txt', 'r').read().split()))]
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
cb = CallbackData('post', 'msg_text')
root_id = None
cur_group = None
groups = {}

'''
Необходимо протестировать все реализованные команды.
Переработать логику работы с root (добавить в поле класса Group, запретить удаление чужой группы)
Доработать остальные команды
'''

async def set_commands() -> None:
    await dp.bot.set_my_commands([
        types.BotCommand("add_group", "Добавить группу"),
        types.BotCommand("choose_group_for_settings", "Выбрать группу для настройки"),
        types.BotCommand("set_quantity_of_people", "Указать число людей в группе"),
        types.BotCommand("add_list_of_group", "Добавить список участников"),
        types.BotCommand("add_list_of_subject", "Добавить лист предметов"),
        types.BotCommand("del_group", "Удалить группу"),
        types.BotCommand("del_list_of_group", "Удалить список участников"),
        types.BotCommand("del_list_of_subject", "Удалить список предметов"),
    ])

def add_button_back_to_menu(buttons) -> list:
    return buttons.append(types.KeyboardButton('Вернуться в главное меню'))

@dp.message_handler(commands=['start', 'back_to_main'])
async def start_handler(message: types.Message) -> None:
    text = ''
    if message.text == '/start':
        text = f'Привет, {message.from_user.first_name}'
    else:
        text = 'Вы вернулись в главное меню'

    markup_for_greetings_text = types.ReplyKeyboardMarkup()
    button_for_help = types.KeyboardButton('Помощь')
    button_for_choose_subject = types.KeyboardButton('Записаться в очередь')
    markup_for_greetings_text.add(button_for_help, button_for_choose_subject)
    await bot.send_message(chat_id=message.from_user.id, text=text, reply_markup=markup_for_greetings_text)

@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message) -> None:
    if message.from_user.id in root_id:
        await set_commands()

    url_of_git_rep = 'https://github.com/mityaiii/QueuePythonBot.git'
    text = (
        f"""
    Привет, {message.from_user.first_name}, это бот, который помогает организовать очередь.

    Мой исходный код вы можете найти по ссылке {url_of_git_rep}. Если есть желания помочь или доработать бота, то просьба добавлять все в ведку develop и делать pull request в main.

Что я умею:
    1. Добавлять новую группу (add_group).
    2. Добавлять список группы (add_list).
    3. Хранить текущую очередь.
    """)    
    await bot.send_message(chat_id=message.from_user.id, text=text)

@dp.message_handler(commands=['choose_group_for_settings'])
async def choose_group_for_settings(message: types.Message) -> None:
    text = None
    global cur_group
    number_of_group = message.text.split()[1]
    if number_of_group in groups:
        text = 'Вы выбрали {number_of_group} для настройки'
        cur_group = number_of_group
    else:
        text = 'Такая группа не была найдена'
    
    await bot.send_message(chat_id=message.from_user.id, text=text)

def add_in_groups(name_of_groups) -> None:
    for name in name_of_groups:
        groups[name] = Group()

@dp.message_handler(commands=['add_group'])
async def add_group_with_command(message: types.Message) -> None:
    text_from_message = message.text.split() 
    name_of_groups = [text_from_message[i] for i in range(1, len(text_from_message))]
    text = None

    if name_of_groups == None:
        text = 'Введите название групп через пробел'
        return

    add_in_groups(name_of_groups)
    cur_group = name_of_groups[len(name_of_groups) - 1]
    if len(name_of_groups) == 1:
        text = 'Группа {name_of_groups[0]} была добавлена'
    else:
        text = 'Группы {name_of_group[0]} были добавлены'
        for i in name_of_groups:
            text += ', ' + i
        text += ' были добавлены' 

    await bot.send_message(chat_id=message.from_user.id, text=text)

@dp.message_handler(commands=['set_quantity_of_people'])
async def set_of_quantity_of_people(message: types.Message):
    pass

@dp.message_handler(commands=['add_list_of_group'])
async def add_list_of_group_with_command(message: types.Message):
    pass

def add_list_of_subjects(name_of_group, name_of_subjects):
    groups[name_of_group].add_subject(name_of_subjects)

@dp.message_handler(commands=['add_list_of_subject'])
async def add_list_of_subject_with_command(message: types.Message) -> None:
    text_from_message = message.text.split()
    name_of_group = text_from_message[1]
    number_of_person_in_group = text_from_message[2]
    text = None
    if number_of_person_in_group.isdigit():
        number_of_person_in_group = int(number_of_person_in_group)
        name_of_subjects = [text_from_message[i] for i in range(3, len(text_from_message))]
    else:
        text = 'Введите номер группы'

    if not (name_of_group in groups):
        text = 'Не найдено такой группы'
        return
    
    groups[name_of_group].add_subject()

    if name_of_subjects == None:
        text = 'Вы не указали предмет, который необходимо добавить'
    else:
        text = 'Вы добавили {name_of_subjects[0]}'
        for name in range(1, len(name_of_subjects)):
            text += ', ' + name
    
    await bot.send_message(chat_id=message.from_user.id, text=text)

@dp.message_handler(commands=['give_root'])
async def give_root():
    pass

@dp.message_handler(commands=['del_group'])
async def del_group_with_command(message: types.Message):
    pass

@dp.message_handler(commands=['del_list_of_group'])
async def del_list_of_group_with_command(message: types.Message):
    pass

@dp.message_handler(commands=['del_list_of_subject'])
async def del_list_of_subject_with_command(message: types.Message):
    pass

@dp.message_handler(commands=['del_root'])
async def del_root(message: types.Message):
    name_of_person = message.text.split()[1]

@dp.message_handler(content_types=['text'])
async def handler_for_text(message: types.Message) -> None:
    if message.text == 'Вернуться в главное меню':
        await start_handler(message=message)
    elif message.text in []:
        pass
    elif message.text == 'Записаться в очередь':
        buttons = []
        add_button_back_to_menu(buttons=buttons)
        markup_with_subject = types.ReplyKeyboardMarkup()
        markup_with_subject.add(*buttons)
        await bot.send_message(chat_id=message.from_user.id, text='Выберите предмет', reply_markup=markup_with_subject)
    elif message.text == 'Помощь':
        await help_handler(message=message)
    else:
        await bot.send_message(chat_id=message.from_user.id, text='Я не знаю такой команды.')

def main() -> None:
    # get_primary_info('list_of_group/primary_info.txt')
    executor.start_polling(dp)

if __name__ == '__main__':
    main()