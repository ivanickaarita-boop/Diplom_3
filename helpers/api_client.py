import requests

from helpers import api_urls


class StellarBurgersApi:
    @staticmethod
    def create_user(user_data):
        return requests.post(api_urls.REGISTER_USER, json=user_data)

    @staticmethod
    def delete_user(access_token):
        return requests.delete(
            api_urls.DELETE_USER,
            headers={"Authorization": access_token},
        )