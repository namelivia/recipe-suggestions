import requests


class Recipes:
    URL = "https://www.themealdb.com/api/json/v1/1/random.php"

    @staticmethod
    def random() -> dict:
        return requests.get(Recipes.URL).json()
