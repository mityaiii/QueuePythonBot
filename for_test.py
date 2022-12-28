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
    groups[Group.cur_group].number_of_people_in_group = 30
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
    groups[Group.cur_group].add_person_in_queue(name, id, name_of_subjects, index)

    # Получение информация из класса Group
    # print(groups[Group.cur_group].__dict__)
    # print(groups[Group.cur_group].get_subjects())
    # print(groups[Group.cur_group].people_with_roots)
    # print(groups[Group.cur_group].get_info_about_person_by_index('Алгоритмы', 1).name_of_person)

    print(type(groups[Group.cur_group]))

    return groups

def how_load_to_database():
    d = {'own' : 1, 'two' : 2}
    file = open('list_of_group/info_about_queue.json', 'r+')
    json.dump(d, file, indent=3)    
    # file = FileManager.FileManager()
    # file.open_file('list_of_group/info_about_queue.json', 'w')
    pass
def main():
    how_use_programm()
    # how_load_to_database()

if __name__ == '__main__':
    main()