import random


class View:
    """ The purpose of the view is to compose the responses
    to the user messages. It contains methods that would take data from the
    external API as well as stock responses to facilitate the communication."""

    def __init__(self):
        pass

    def compose_start_message(self, username):
        return f"Hello, {username}! My name is NutrioBot and my role is to provide you with " \
               f"nutritional information and give you healthy recipes! Please let me know which of these you need." + \
            u"\U0001F60B"

    def compose_nutritional_information_request_message(self):
        return "What product would you like to know the nutritional value of? (please write it in the format:\n" \
               "quantity, measure, food, e.g. 1 cup cooked rice)\n You will recieve back information such as " \
               "calories, macronutrients and allergens. "

    def compose_nutritional_information_response_message(self, response_json):
        return f"Here is the data for {response_json['ingredients'][0]['text']}:\n" \
               f"Calories: {response_json['calories']}\n" \
               f"Nutrients:\n" \
               f" - Fat: {response_json['totalNutrients']['FAT']['quantity']} " \
               f"{response_json['totalNutrients']['FAT']['unit']}\n" \
               f"    of which saturated: {response_json['totalNutrients']['FASAT']['quantity']} " \
               f"{response_json['totalNutrients']['FASAT']['unit']}\n" \
               f" - Carbohydrates (net): {response_json['totalNutrients']['CHOCDF.net']['quantity']} " \
               f"{response_json['totalNutrients']['CHOCDF.net']['unit']}\n "\
                f" - Protein: {response_json['totalNutrients']['PROCNT']['quantity']} " \
               f"{response_json['totalNutrients']['PROCNT']['unit']}\n" \
               f" - Sodium: {response_json['totalNutrients']['NA']['quantity']} " \
               f"{response_json['totalNutrients']['NA']['unit']}\n" \
               f"Would you like nutritional information about something else or perhaps a recipe? " + \
                u"\U0001F60A"


    def compose_returned_recipe_response_message(self, response_json, recipe):
            finalized_string = f"Here is a recipe with your selected ingredients - {response_json['q']}\n" \
               f"{recipe['label']} - {recipe['url']}\n" \
               f"Would you like to save it?"
            return finalized_string

