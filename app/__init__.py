import falcon
from app.resources import ProductResource
from falcon import App


class Application():
    def __init__(self) -> None:
        self.__app = falcon.App()
        self.__app.add_route('/', ProductResource())

    def create_instance(self) -> App:
        return self.__app
