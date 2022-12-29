class Subject:
    cur_queue = []
    def __init__(self, quantity_of_people_in_group) -> None:
        self.quantity_of_people_in_group = quantity_of_people_in_group
        self.cur_queue = [0] * quantity_of_people_in_group

    def del_list_of_people(self, ind_of_people_in_queue):
        for ind_person in ind_of_people_in_queue:
            self.cur_queue[int(ind_person)] = 0
