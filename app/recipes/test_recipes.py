from unittest import TestCase
from .recipes import Recipes
import mock


class TestRecipes(TestCase):
    @mock.patch("app.recipes.recipes.requests")
    def test_getting_random(self, m_requests):
        m_requests.get.return_value.json.return_value = {"meals": []}
        random = Recipes.random()
        m_requests.get.assert_called_once_with(
            "https://www.themealdb.com/api/json/v1/1/random.php"
        )
        assert random == {"meals": []}
