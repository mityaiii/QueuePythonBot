cur_group = None

class Group:
    __people_with_roots = None

    class __Person:
        name_of_person = None
        id = None
        root_mode = False

        def __init__(self, name_of_person, id) -> None:
            self.name_of_person = name_of_person
            self.id = id

    class __Subject:
        number_of_people_in_group = None
        cur_queue = []
        def __init__(self, number_of_people_in_group) -> None:
            self.number_of_people_in_group = number_of_people_in_group
            self.cur_queue = [0] * number_of_people_in_group
    
    __subjects = {}
    __number_of_people_in_group = 0

    @property
    def people_with_roots(self) -> list:
        return self.__people_with_roots
    
    @people_with_roots.setter
    def people_with_roots(self, people_with_roots) -> None:
        self.__people_with_roots = people_with_roots

    @property
    def number_of_people_in_group(self) -> int:
        return self.__number_of_people_in_group

    @number_of_people_in_group.setter
    def number_of_people_in_group(self, number_of_people_in_group) -> None:
        self.__number_of_people_in_group = number_of_people_in_group

    def add_subjects(self, name_of_subjects) -> None:
        for name_of_subject in name_of_subjects:        
            subject = self.__Subject(self.__number_of_people_in_group)
            self.__subjects[name_of_subject] = subject

    def get_subjects(self) -> dict:
        return self.__subjects

    def get_queue_from_subjec(self, name_of_subject) -> list:
        return self.__subjects[name_of_subject].cur_queue

    def add_person_in_queue(self, name_of_person, id, name_of_subjects, index) -> None:
        person = self.__Person(name_of_person, id)
        self.__subjects[name_of_subjects].cur_queue[index] = person

    def get_dist_of_subjects(self) -> dict:
        return self.__subjects
    
    def get_info_about_person_by_index(self, name_of_subjects, index_of_person):
        return self.__subjects[name_of_subjects].cur_queue[index_of_person]
    
    def get_info_about_person_by_name(self, name_of_subjects, name_of_person):
        return self.__subjects[name_of_subjects].cur_queue.find(name_of_person)

    def remove_list_of_subjects(self, names_of_subject):
        for name_of_subject in names_of_subject:
            self.__subjects.remove(name_of_subject)
    
    def is_subject_exist(self, name_of_subject):
        return name_of_subject in self.__subjects