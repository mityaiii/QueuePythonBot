class Person:
    name_of_person = None
    id = None
    root_mode = False

    def __init__(self, name_of_person, id) -> None:
        self.name_of_person = name_of_person
        self.id = id