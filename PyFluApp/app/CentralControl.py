from structure.Config import Config


class CentralControl:

    def __init__(self, main_app: tuple):
        self.__config = Config()
        self.__central = main_app[0], main_app[1], main_app[2], self.__config


    def __getitem__(self, item):
        return self.__central[int(item)]

