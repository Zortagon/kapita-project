import falcon
import app.resources as resources
from falcon import App


class Application():
    def __init__(self) -> None:
        self.__app = falcon.App()
        self.__app.add_route('/', resources.Products())

    def create_instance(self) -> App:
        return self.__app
