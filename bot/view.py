
class View:

    """ The purpose of the view is to compose the responses
    to the user messages. It contains methods that would take data from the
    external API as well as stock responses to facilitate the communication."""
    def __init__(self):
        pass

    def compose_start_message(self, username):
        return f"Hello, {username}! My name is NutrioBot and my role is to provide you with " \
               f"nutritional information, give you healthy recipes and keep track of food-related reminders!"


    def compose_nutritional_information_request_message(self):
        return "What product would you like to know the nutritional value of? (please write it in the format" \
               "quantity, measure, food, e.g. 1 cup cooked rice) You will recieve back information such as " \
               "calories, macronutrients and allergens. "
