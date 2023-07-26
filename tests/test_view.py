# tests/test_view.py
import unittest
from telegram_nutrio.view import View


class TestView(unittest.TestCase):

    def setUp(self):
        self.view = View()

    def test_compose_start_message(self):
        username = "TestUser"
        expected_message = f"Hello, {username}! My name is NutrioBot and my role is to provide you with " \
                           f"nutritional information and give you healthy recipes! Please let me know which " \
                           f"of these you need.\U0001F60B"
        result = self.view.compose_start_message(username)
        self.assertEqual(result, expected_message)

    def test_compose_nutritional_information_request_message(self):
        expected_message = "What product would you like to know the nutritional value of? " \
                           "(please write it in the format:\nquantity, measure, food, e.g. 1 cup cooked rice)\n " \
                           "You will receive back information such as calories, macronutrients, and allergens. "
        result = self.view.compose_nutritional_information_request_message()
        self.assertEqual(result, expected_message)

    def test_compose_nutritional_information_response_message(self):
        # Mock API response JSON for testing
        response_json = {
            "ingredients": [{"text": "Test Ingredient"}],
            "totalNutrients": {
                "Nutrient 1": {"label": "Nutrient 1", "quantity": 100, "unit": "g"},
                "Nutrient 2": {"label": "Nutrient 2", "quantity": 50, "unit": "mg"}
            }
        }
        expected_message = "Here is the data for Test Ingredient:\nNutrient 1: 100 g, \nNutrient 2: 50 mg\n" \
                           "Would you like nutritional information about something else or perhaps a recipe? \U0001F60A"
        result = self.view.compose_nutritional_information_response_message(response_json)
        self.assertEqual(result, expected_message)


if __name__ == "__main__":
    unittest.main()
