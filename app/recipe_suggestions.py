import os
from dotenv import load_dotenv
from app.formatting.formatting import Formatting
from app.recipes.recipes import Recipes
from app.notifications.notifications import Notifications


class RecipeSuggestions:
    @staticmethod
    def run():
        load_dotenv()
        recipe = Recipes.random()
        Notifications.send(Formatting.format(recipe["meals"][0]))
