class View:
    """ The purpose of the view is to compose the responses
    to the user messages. It contains methods that would take data from the
    external API as well as stock responses to facilitate the communication."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True

    def compose_start_message(self, username):
        return f"Hello, {username}! My name is NutrioBot and my role is to provide you with " \
               f"nutritional information and give you healthy recipes! Please let me know which of these you need." + \
            u"\U0001F60B"

    def compose_nutritional_information_request_message(self):
        return "What product would you like to know the nutritional value of? (please write it in the format:\n" \
               "quantity, measure, food, e.g. 1 cup cooked rice)\n You will recieve back information such as " \
               "calories, macronutrients and allergens. "

    def compose_nutritional_information_response_message(self, response_json):
        nutrient_info_list = []
        for nutrient_key, nutrient_data in response_json["totalNutrients"].items():
            label = nutrient_data['label']
            quantity = nutrient_data['quantity']
            unit = nutrient_data['unit']
            nutrient_info_list.append(f"{label}: {quantity} {unit}")
        final_string = ", \n".join(nutrient_info_list)
        return f"Here is the data for {response_json['ingredients'][0]['text']}:\n" \
               f"{final_string}\n" \
               f"Would you like nutritional information about something else or perhaps a recipe? " + \
            u"\U0001F60A"

    def compose_recipe_request_message(self):
        return f"What ingredients should your recipe recommendations contain? Please list them separated by commas " \
               f"(eg. chicken, butter, tomatoes)."

    def compose_returned_recipe_response_message(self, response_json, recipe_list):
        recipe_string = ""
        for recipe in recipe_list[:11]:
            recipe_string += f"{recipe['recipe']['label']} - {recipe['recipe']['url']}\n"
        finalized_string = f"Here are some recipes with your selected ingredients - {response_json['q']}\n" \
                           f"{recipe_string}" \
                           f"Would you a recipe with different ingredients or perhaps" \
                           f" the nutritional values of a food?" + \
                           u"\U0001F60A"
        return finalized_string

    def compose_recipe_not_found_message(self):
        return f"Uh oh! No recipe was found with those parameters. Please try again with different ingredients."

    def compose_nutrition_information_not_found_message(self):
        return "Uh oh! No such food was found in the database. Please try again with a different one!"

    def compose_cancel_message(self):
        return f'Sorry to see you go! If you would like to have a look at the nutrition of an ingredient or check out ' \
               f'a recipe, you can do by selecting the /start command. Bye!'
