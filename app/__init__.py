from falcon import App
import falcon


class Application():
    def __init__(self) -> None:
        self.__app = falcon.App()

    def create_instance(self) -> App:
        return self.__app
