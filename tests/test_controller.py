import unittest
from unittest.mock import patch, MagicMock

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from telegram_nutrio.controller import Controller
from telegram_nutrio.Model.edamam_API_connection import EdamameConnector



class TestController(unittest.TestCase):

    def setUp(self):
        self.controller = Controller()
        self.api_connector = EdamameConnector()

    def test_handle_start_command(self):
        update = MagicMock()
        update.message.chat.username = "test_user"
        expected_response = "Hello, test_user! My name is NutrioBot and my role is to provide you with nutritional " \
                            "information and give you healthy recipes! Please let me know which of these you need.😋"

        response = self.controller.handle_start_command(update)
        self.assertEqual(response, expected_response)

    def test_handle_request_nutritional_information_command(self):
        expected_response = "What product would you like to know the nutritional value of? (please write it in the " \
                            "format: quantity, measure, food, e.g. 1 cup cooked rice). You will recieve back " \
                            "information such as calories, macronutrients and allergens."
        response = self.controller.handle_request_nutritional_information_command()
        self.assertEqual(response, expected_response)

    @patch('controller.EdamameConnector')
    def test_handle_user_input_nutritional_information(self, mock_connector):
        update = MagicMock()
        update.message.text = "1 cup cooked rice"
        mock_connector.return_value.request_nutritional_information.return_value = {
            "totalNutrients": {
                "Calories": {"label": "Calories", "quantity": 100, "unit": "kcal"},
                "Protein": {"label": "Protein", "quantity": 5, "unit": "g"},
                "Carbohydrates": {"label": "Carbohydrates", "quantity": 20, "unit": "g"},
            },
            "ingredients": [{"text": "1 cup cooked rice"}]
        }
        expected_response = "Here is the data for 1 cup cooked rice:\nCalories: 100 kcal, \nProtein: 5 g, " \
                            "\nCarbohydrates: 20 g\nWould you like nutritional information about something else or " \
                            "perhaps a recipe? 😊"

        response = self.controller.handle_user_input_nutritional_information(update)
        self.assertEqual(response, expected_response)

    def test_handle_request_recipe_command(self):
        expected_response = "What ingredients should your recipe recommendations contain?" \
                            " Please list them separated by commas (e.g. chicken, butter, tomatoes)."
        response = self.controller.handle_request_recipe_command()
        self.assertEqual(response, expected_response)

    @patch('controller.EdamameConnector')
    def test_handle_recipe_request(self, mock_connector):
        update = MagicMock()
        update.message.text = "chicken, butter, tomatoes"
        mock_connector.return_value.request_recipe_information.return_value = {
            "count": 3,
            "hits": [
                {"recipe": {"label": "Recipe 1", "url": "https://example.com/recipe1"}},
                {"recipe": {"label": "Recipe 2", "url": "https://example.com/recipe2"}},
                {"recipe": {"label": "Recipe 3", "url": "https://example.com/recipe3"}},
            ]
        }
        expected_response = "Here are some recipes with your selected ingredients - chicken, butter, tomatoes\nRecipe " \
                            "1 - https://example.com/recipe1\nRecipe 2 - https://example.com/recipe2\nRecipe 3 - " \
                            "https://example.com/recipe3\nWould you a recipe with different ingredients or perhaps " \
                            "the nutritional values of a food? 😊"

        response = self.controller.handle_recipe_request(update)
        self.assertEqual(response, expected_response)

    def test_handle_cancel_message(self):
        expected_response = "Sorry to see you go! If you would like to have a look at the nutrition of an ingredient or check out a recipe, " \
                            "you can do so by selecting the /start command. Bye!"
        response = self.controller.handle_cancel_message()
        self.assertEqual(response, expected_response)


if __name__ == '__main__':
    unittest.main()
