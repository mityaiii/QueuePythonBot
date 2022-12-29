import Group
import FileManager
import json

def how_use_programm() -> dict:
    groups = {}
    # Выбрать группу для изменения
    Group.cur_group = '05'
    # Создания группы
    group = Group.Group()
    groups[Group.cur_group] = group
    # Количество людей в группе 
    groups[Group.cur_group].quantity_of_people_in_group = 30
    # Задание предметов
    subjects = ['Основы программирования', 'Алгоритмы']
    groups[Group.cur_group].add_subjects(subjects)
    # Задание людей с root правами
    people_with_roots = ['1', '2']
    groups[Group.cur_group].people_with_roots = people_with_roots
    # Заполнение группы
    name = 'Геша'
    id = 123
    name_of_subjects = 'Алгоритмы'
    index = 1
    groups[Group.cur_group].add_person_to_queue(name, id, name_of_subjects, index)

    # Получение информация из класса Group
    groups[Group.cur_group].get_info_about_group()

    return groups

def how_load_to_database():
    data = {}
    file = open('channel_users.json', 'r+', encoding='utf-8')
    data = json.load(file)
    print(data)

def test(d):
    print(id(d))

def main():
    # how_use_programm()
    # how_load_to_database()
    a = {}
    print(id(a))
    test(a)

if __name__ == '__main__':
    main()