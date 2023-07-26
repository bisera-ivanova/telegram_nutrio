import os
from py_edamam import Edamam
from dotenv import load_dotenv

load_dotenv("credentials.env")

class EdamameConnector:
    """The EdamameConnector class handles the communication with the Edamam API to request
    nutritional information and recipe data based on user input."""

    _instance = None

    def __new__(cls):
        """Creates a singleton instance of the EdamameConnector class.

        Returns:
            EdamameConnector: The singleton instance of the EdamameConnector class.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        """Initialize the EdamameConnector.

        The EdamameConnector creates an instance of Edamam for API communication
        using the provided credentials from the environment variables.
        """
        self.edamam_api_connector = Edamam(nutrition_appid=os.getenv('EDAMAM_NUTRITION_API_ID'),
                                           nutrition_appkey=os.getenv('EDAMAM_NUTRITION_API_KEY'),
                                           recipes_appkey=os.getenv('EDAMAM_RECIPE_API_KEY'),
                                           recipes_appid=os.getenv('EDAMAM_RECIPE_API_ID'))
        if self.__initialized:
            return
        self.__initialized = True

    def request_nutritional_information(self, user_input):
        """Request nutritional information from the Edamam API based on user input.

        Args:
            user_input (str): User input specifying the product for which nutritional information is requested.

        Returns:
            dict: A dictionary containing the nutritional data of the specified product.
        """
        nutritional_data = self.edamam_api_connector.search_nutrient(user_input.strip().lower())
        return nutritional_data

    def request_recipe_information(self, user_input):
        """Request recipe information from the Edamam API based on user input.

        Args:
            user_input (str): User input specifying the recipe or ingredients for which recipe information is requested.

        Returns:
            dict: A dictionary containing recipe data matching the user input.
        """
        recipes = self.edamam_api_connector.search_recipe(user_input.strip().lower())
        return recipes

