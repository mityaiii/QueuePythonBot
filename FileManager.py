import json

class FileManager:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(FileManager, cls).__new__(cls)
        return cls.__instance

    __file = None

    def __is_open(self) -> bool:
        if self.__file is None:
            return False
        return not self.__file.closed

    def open_file(self, name_of_file) -> None:
        if not self.__is_open():
            self.__file = open(name_of_file, 'r+')

    def load_info_to_file(self, info):
        if self.__is_open():
            json.dump(info, self.__file, indent=2)

    def get_dict_from_file(self) -> dict:
        if self.__is_open():
            return self.__file.read()
        return None

    def close_file(self) -> None:
        if not self.__is_open():
            self.__file.close()
