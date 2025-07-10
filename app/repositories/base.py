from tortoise import Tortoise


class BaseRepository:

    def __init__(self):
        self.connection = Tortoise.get_connection("default")
