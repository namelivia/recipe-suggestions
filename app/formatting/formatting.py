import logging

logger = logging.getLogger(__name__)


class Formatting:
    @staticmethod
    def format(recipe: dict) -> str:
        name = recipe["strMeal"]
        url = recipe["strSource"]
        return f"{name}: {url}"
