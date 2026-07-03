from uuid import uuid4


class UserData:
    PASSWORD = "Password123"
    NAME = "Margarita"

    @staticmethod
    def get_unique_user():
        return {
            "email": f"margarita_{uuid4()}@yandex.ru",
            "password": UserData.PASSWORD,
            "name": UserData.NAME,
        }