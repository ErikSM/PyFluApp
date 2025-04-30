
from app.AppBody import AppBody
from app.AppFoot import AppFoot
from app.AppHead import AppHead

from structure.Config import Config


class CentralControl:

    def __init__(self, head: AppHead, body: AppBody, foot: AppFoot):
        self.__config = Config()

        self.__central = head, body, foot, self.__config

    def __getitem__(self, item):
        return self.__central[int(item)]






