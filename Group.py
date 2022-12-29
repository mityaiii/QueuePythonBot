import Person
import Subject

cur_group = None

class Group:
    people_with_roots = None    
    __subjects = {}
    quantity_of_people_in_group = 0

    def add_subjects(self, name_of_subjects) -> None:
        for name_of_subject in name_of_subjects:        
            subject = Subject.Subject(self.quantity_of_people_in_group)
            self.__subjects[name_of_subject] = subject

    def get_queue_from_subject(self, name_of_subject) -> list:
        return self.__subjects[name_of_subject].cur_queue

    def add_person_to_queue(self, name_of_person, id, name_of_subjects, index) -> None:
        person = Person.Person(name_of_person, id)
        print(len(self.__subjects[name_of_subjects].cur_queue))
        self.__subjects[name_of_subjects].cur_queue[index] = person

    def get_list_of_subjects(self) -> dict:
        return self.__subjects
    
    def get_info_about_person_by_index(self, name_of_subjects, index_of_person) -> Person.Person:
        return self.__subjects[name_of_subjects].cur_queue[index_of_person]
    
    def get_info_about_person_by_name(self, name_of_subjects, name_of_person) -> Person.Person:
        return self.__subjects[name_of_subjects].cur_queue.find(name_of_person)

    def remove_list_of_subjects(self, names_of_subject):
        for name_of_subject in names_of_subject:
            self.__subjects.remove(name_of_subject)
    
    def is_subject_exist(self, name_of_subject) -> bool:
        return name_of_subject in self.__subjects

    def get_info_about_group(self, name_of_group=cur_group):
        print(name_of_group)
        print(f'количество людей {self.quantity_of_people_in_group}')
        print(f'людей с root {self.people_with_roots}')
        print(f'список предметов {self.get_list_of_subjects()}')
        for subject in self.get_list_of_subjects():
            print(f'очередь на {subject}: {self.get_queue_from_subject(subject)}')

    def __del_list(self, dict_for_del, list_for_del) -> None:
        for name in list_for_del:
            dict_for_del.pop(name, 'Не удалось удалить объект')
    
    def del_list_of_subjects(self, list_of_subjects) -> None:
        self.__del_list(self.__subjects, list_of_subjects)

    def del_list_of_people_with_roots(self, people_with_roots):
        self.__del_list(self.people_with_roots, people_with_roots)

    def del_list_of_person_in_subject(self, name_of_subject, ind_of_people_in_queue):
        self.__subjects[name_of_subject].del_list_of_people(ind_of_people_in_queue)    

    