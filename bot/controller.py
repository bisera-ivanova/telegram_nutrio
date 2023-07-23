from telegram_nutrio.Model.edamam_API_connection import EdamameConnector
from . import view


class Controller:

    def __init__(self):
        self.api_connector = EdamameConnector()
        self.view = view.View()

    def handle_start_command(self, update):
        return self.view.compose_start_message(update.message.chat.username)

    def handle_request_nutritional_information_command(self):
        return self.view.compose_nutritional_information_request_message()

    def handle_user_input_nutritional_information(self, update):
        try:
            nutritional_information_json = self.api_connector.request_nutritional_information(update.message.text)
            response_message = self.view.compose_nutritional_information_response_message(nutritional_information_json)
            return response_message
        except Exception:
            return self.view.compose_nutrition_information_not_found_message()

    def handle_request_recipe_command(self):
        return self.view.compose_recipe_request_message()

    def handle_recipe_request(self, update):
        recipe_information = self.api_connector.request_recipe_information(update.message.text)
        if recipe_information["count"] == 0:
            return self.view.compose_recipe_not_found_message()
        recipe_list = recipe_information['hits']
        return self.view.compose_returned_recipe_response_message(recipe_information, recipe_list)

    def handle_cancel_message(self):
        return self.view.compose_cancel_message()
