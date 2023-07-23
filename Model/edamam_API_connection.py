import os

from py_edamam import Edamam
from dotenv import load_dotenv


load_dotenv("credentials.env")


class EdamameConnector:

    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        self.edamam_api_connector = Edamam(nutrition_appid=os.getenv('EDAMAM_NUTRITION_API_ID'),
                                           nutrition_appkey=os.getenv('EDAMAM_NUTRITION_API_KEY'),
                                           recipes_appkey=os.getenv('EDAMAM_RECIPE_API_KEY'),
                                           recipes_appid=os.getenv('EDAMAM_RECIPE_API_ID'))
        if self.__initialized:
            return
        self.__initialized = True

    def request_nutritional_information(self, user_input):
        nutritional_data = self.edamam_api_connector.search_nutrient(user_input.strip().lower())
        return nutritional_data

    def request_recipe_information(self, user_input):
        recipes = self.edamam_api_connector.search_recipe(user_input.strip().lower())
        return recipes
