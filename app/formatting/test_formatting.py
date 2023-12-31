from unittest import TestCase
from .formatting import Formatting
import json


class TestFormatting(TestCase):
    def test_formatting(self):
        data = {
            "idMeal": "52814",
            "strMeal": "Thai Green Curry",
            "strDrinkAlternate": None,
            "strCategory": "Chicken",
            "strArea": "Thai",
            "strInstructions": "Put the potatoes in a pan of boiling water and cook for 5 minutes. Throw in the beans and cook for a further 3 minutes, by which time both should be just tender but not too soft. Drain and put to one side.\r\nIn a wok or large frying pan, heat the oil until very hot, then drop in the garlic and cook until golden, this should take only a few seconds. Don\u2019t let it go very dark or it will spoil the taste. Spoon in the curry paste and stir it around for a few seconds to begin to cook the spices and release all the flavours. Next, pour in the coconut milk and let it come to a bubble.\r\nStir in the fish sauce and sugar, then the pieces of chicken. Turn the heat down to a simmer and cook, covered, for about 8 minutes until the chicken is cooked.\r\nTip in the potatoes and beans and let them warm through in the hot coconut milk, then add a lovely citrussy flavour by stirring in the shredded lime leaves (or lime zest). The basil leaves go in next, but only leave them briefly on the heat or they will quickly lose their brightness. Scatter with the lime garnish and serve immediately with boiled rice.",
            "strMealThumb": "https:\/\/www.themealdb.com\/images\/media\/meals\/sstssx1487349585.jpg",
            "strTags": "Curry,Mild",
            "strYoutube": "https:\/\/www.youtube.com\/watch?v=LIbKVpBQKJI",
            "strIngredient1": "potatoes",
            "strIngredient2": "green beans",
            "strIngredient3": "sunflower oil",
            "strIngredient4": "garlic",
            "strIngredient5": "Thai green curry paste",
            "strIngredient6": "coconut milk",
            "strIngredient7": "Thai fish sauce",
            "strIngredient8": "Sugar",
            "strIngredient9": "Chicken",
            "strIngredient10": "lime",
            "strIngredient11": "basil",
            "strIngredient12": "Rice",
            "strIngredient13": "",
            "strIngredient14": "",
            "strIngredient15": "",
            "strIngredient16": "",
            "strIngredient17": "",
            "strIngredient18": "",
            "strIngredient19": "",
            "strIngredient20": "",
            "strMeasure1": "225g new",
            "strMeasure2": "100g ",
            "strMeasure3": "1 tbsp",
            "strMeasure4": "1 clove",
            "strMeasure5": "4 tsp ",
            "strMeasure6": "400ml",
            "strMeasure7": "2 tsp",
            "strMeasure8": "1 tsp",
            "strMeasure9": "450g boneless",
            "strMeasure10": "2 fresh kaffir leaves",
            "strMeasure11": "handfull",
            "strMeasure12": "Boiled",
            "strMeasure13": "",
            "strMeasure14": "",
            "strMeasure15": "",
            "strMeasure16": "",
            "strMeasure17": "",
            "strMeasure18": "",
            "strMeasure19": "",
            "strMeasure20": "",
            "strSource": "http:\/\/www.bbcgoodfood.com\/recipes\/3235\/thai-green-chicken-curry",
            "strImageSource": None,
            "strCreativeCommonsConfirmed": None,
            "dateModified": None,
        }
        formatted_message = Formatting.format(data)
        assert (
            formatted_message
            == "Thai Green Curry: http:\/\/www.bbcgoodfood.com\/recipes\/3235\/thai-green-chicken-curry"
        )
