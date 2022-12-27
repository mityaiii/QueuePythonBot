import Group
import FileManager

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.callback_data import CallbackData

__info = open('list_of_group/primary_info.txt', 'r').read().split()

TOKEN = __info[0]
root_id = [int(__info[i]) for i in range(1, len(__info))]
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
cb = CallbackData('post', 'msg_text')
groups = {}

'''
План

Необходимо протестировать все реализованные команды.
Необходимо научиться загружать в json, используя .json
Переработать логику работы с root (добавить в поле класса Group, запретить удаление чужой группы) +
Доработать остальные команды
Разработать логики нажатия клавиш

'''

def get_list_without_command(message: types.Message) -> list:
    text_from_message = message.text.split()
    list_without_command = text_from_message[1 : len(text_from_message)]
    return list_without_command

async def set_commands_in_menu(my_commands) -> None:

    list_of_my_commands = [types.BotCommand(command[0], command[1]) for command in my_commands.items()]
    await dp.bot.set_my_commands(list_of_my_commands)    

@dp.message_handler(commands=['give_root'])
async def give_root_with_command(message: types.Message) -> None:
    groups[Group.cur_group].people_with_roots = await get_list_without_command(message=message)


def add_button_back_to_menu(buttons) -> list:
    return buttons.append(types.KeyboardButton('Вернуться в главное меню'))

@dp.message_handler(commands=['start', 'back_to_main'])
async def start_handler(message: types.Message) -> None:
    text = None
    if message.text == '/start':
        text = f'Привет, {message.from_user.first_name}'
    else:
        text = 'Вы вернулись в главное меню'

    markup_for_greetings_text = types.ReplyKeyboardMarkup()
    button_for_help = types.KeyboardButton('Помощь')
    button_for_choose_subject = types.KeyboardButton('Записаться в очередь')
    markup_for_greetings_text.add(button_for_help, button_for_choose_subject)
    await bot.send_message(chat_id=message.from_user.id, text=text, reply_markup=markup_for_greetings_text)

async def set_root_commands() -> dict:
    my_commands = {
        "choose_group_for_settings": "Выбрать группу для настройки",
        "set_quantity_of_people": "Указать число людей в группе",
        "add_list_of_group": "Добавить список участников",
        "add_list_of_subject": "Добавить лист предметов",
        "del_list_of_group": "Удалить список участников",
        "del_list_of_subject": "Удалить список предметов"
    }
    return my_commands

async def set_god_root_commands() -> dict:
    my_commands = await set_root_commands()
    my_commands["add_group"] = "Добавить группу"
    my_commands["give_root"] = "Выдать пользователю root права"
    my_commands["del_group"] = "Удалить группу"

    return my_commands

@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message) -> None:
    my_commands = None
    if Group.cur_group != None and message.from_user.id in groups[Group.cur_group].people_with_root:
        my_commands = await set_root_commands()
    elif message.from_user.id in root_id:
        my_commands = await set_god_root_commands()

    if not(my_commands is None):
        await set_commands_in_menu(my_commands=my_commands)

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
    number_of_group = message.text.split()[1]
    if number_of_group in groups:
        text = f'Вы выбрали {number_of_group} для настройки'
        Group.cur_group = number_of_group
    else:
        text = 'Такая группа не была найдена'
    
    await bot.send_message(chat_id=message.from_user.id, text=text)

def add_groups(name_of_groups) -> None:
    for name in name_of_groups:
        groups[name] = Group.Group()

@dp.message_handler(commands=['add_group'])
async def add_group_with_command(message: types.Message) -> None:
    name_of_groups = await get_list_without_command(message=message)
    text = None

    if name_of_groups == None:
        text = 'Введите название групп через пробел'
        return

    add_groups(name_of_groups)
    Group.cur_group = name_of_groups[len(name_of_groups) - 1]
    if len(name_of_groups) == 1:
        text = f'Группа {name_of_groups[0]} была добавлена'
    else:
        text = f'Группы {name_of_groups[0]} были добавлены'
        for i in name_of_groups:
            text += ', ' + i
        text += ' были добавлены' 

    await bot.send_message(chat_id=message.from_user.id, text=text)

@dp.message_handler(commands=['set_quantity_of_people'])
async def set_of_quantity_of_people(message: types.Message):
    text_from_message = message.text.split()
    quantity_of_people = text_from_message[1]
    text = None
    if quantity_of_people.isdigit():
        groups[Group.cur_group] = int(quantity_of_people)
        text = f'Теперь в группе находиться {quantity_of_people} человек'
    else:
        text = 'Введите целое число'
    await bot.send_message(chat_id=message.from_user.id, text=text)

def add_list_of_subjects(name_of_subjects):
    groups[Group.cur_group].add_subject(name_of_subjects)

@dp.message_handler(commands=['add_list_of_subject'])
async def add_list_of_subject_with_command(message: types.Message) -> None:
    name_of_subjects = await get_list_without_command(message=message)

    text = None
    if name_of_subjects == None:
        text = 'Вы не указали предмет, который необходимо добавить'
    else:
        text = f'Вы добавили {name_of_subjects[0]}'
        for i in range(1, len(name_of_subjects)):
            text += ', ' + name_of_subjects[i]
    
    await bot.send_message(chat_id=message.from_user.id, text=text)

@dp.message_handler(commands=['del_list_of_group'])
async def del_group_with_command(message: types.Message):
    names_of_group = await get_list_without_command(message=message)
    for name_of_group in names_of_group:
        groups.pop(name_of_group)

@dp.message_handler(commands=['del_list_of_subject'])
async def del_list_of_subject_with_command(message: types.Message):
    groups[Group.cur_group].remove_list_of_subjects(await get_list_without_command(message=message))
    
@dp.message_handler(commands=['del_list_person_with_root'])
async def del_root(message: types.Message):
    groups[Group.cur_group].remove_list_of_subjects(await get_list_without_command(message=message))

@dp.message_handler(content_types=['text'])
async def handler_for_text(message: types.Message) -> None:
    if message.text == 'Вернуться в главное меню':
        await start_handler(message=message)
    elif message.text in ['subject']:
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
    executor.start_polling(dp)

if __name__ == '__main__':
    main()
    # print(groups)
    # print(Group.cur_group)
    # print(groups[Group.cur_group].get_subjects().keys())