class Group:
    people_with_roots = None
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
    def number_of_people_in_group(self, number_of_people_in_group) -> None:
        self.__number_of_people_in_group = number_of_people_in_group
    
    @number_of_people_in_group.setter
    def number_of_people_in_group(self) -> int:
        return self.number_of_people_in_group

    def add_subject(self, name_of_subjects) -> None:        
        subject = self.__Subject(self.__number_of_people_in_group)
        self.__subjects[name_of_subjects] = subject

    def add_person_in_queue(self, name_of_person, id, name_of_subjects, index) -> None:
        person = self.__Person(name_of_person, id)
        self.__subjects[name_of_subjects].cur_queue[index] = person

    @property
    def get_queue_from_subjects(self, name_of_subject) -> list:
        return self.__subjects[name_of_subject].cur_queue

    def get_dist_of_subjects(self) -> dict:
        return self.__subjects
    
    def get_info_about_person_by_index(self, name_of_subjects, index_of_person):
        return self.__subjects[name_of_subjects].cur_queue[index_of_person]
    
    def get_info_about_person_by_name(self, name_of_subjects, name_of_person):
        return self.__subjects[name_of_subjects].cur_queue.find(name_of_person)

    def remove_subject(self, index):
        self.__subjects.remove(index)
    
    def is_subject_exist(self, name_of_subject):
        return name_of_subject in self.__subjects